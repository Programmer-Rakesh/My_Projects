
import os
import cv2
import pickle

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100
img_size = (640, 640)  # Resize to square (640x640) for MediaPipe compatibility

cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'\nCollecting data for class {j}')
    
    # Countdown before starting capture
    for i in range(3, 0, -1):
        print(f"Starting in {i} seconds...")
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame from camera")
            break
        cv2.putText(frame, f'Starting in {i}', (200, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 255), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(1000)  # Wait 1 second

    print("Press 'Q' to start capturing images...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not capture frame from camera")
            break

        cv2.putText(frame, f'Class {j}: Press "Q" to start!', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Could not read frame {counter}, skipping...")
            continue

        frame_resized = cv2.resize(frame, img_size)  # Resize to 640x640
        file_path = os.path.join(class_dir, f"{counter}.jpg")
        success = cv2.imwrite(file_path, frame_resized)
        print(f"Capturing Image {counter} for class {j} - {'Saved' if success else 'Failed'}")

        cv2.putText(frame_resized, f'Class {j}: {counter}/{dataset_size}', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame_resized)
        cv2.waitKey(100)  # Adjust for slower or faster capture speed
        counter += 1

cap.release()
cv2.destroyAllWindows()

# Now, let's create the dataset (pickling the data)
data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_resized = cv2.resize(img, img_size)  # Resize each image
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

        # Assuming you are using MediaPipe for hand landmarks
        hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)

# Save data and labels as pickle
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print("Dataset successfully saved as data.pickle")
