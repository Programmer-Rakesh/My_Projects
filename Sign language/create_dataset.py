# import os
# import pickle

# import mediapipe as mp
# import cv2
# import matplotlib.pyplot as plt


# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles

# hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# DATA_DIR = './data'

# data = []
# labels = []
# for dir_ in os.listdir(DATA_DIR):
#     for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
#         data_aux = []

#         x_ = []
#         y_ = []

#         img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#         results = hands.process(img_rgb)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y

#                     x_.append(x)
#                     y_.append(y)

#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y
#                     data_aux.append(x - min(x_))
#                     data_aux.append(y - min(y_))

#             data.append(data_aux)
#             labels.append(dir_)

# f = open('data.pickle', 'wb')
# pickle.dump({'data': data, 'labels': labels}, f)
# f.close()





import os
import pickle
import mediapipe as mp
import cv2

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True, 
    min_detection_confidence=0.3,
    model_complexity=1  # Reduce complexity to avoid projection issues
)

DATA_DIR = './data'
IMG_SIZE = 640  # Ensure consistency with dataset collection

data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    if not os.path.isdir(dir_path):  # Skip non-directory files
        continue

    for img_path in os.listdir(dir_path):
        data_aux = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(dir_path, img_path))
        if img is None:
            print(f"Warning: Unable to read image {img_path}")
            continue

        img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  # Ensure image is square
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x_.append(hand_landmarks.landmark[i].x * IMG_SIZE)
                    y_.append(hand_landmarks.landmark[i].y * IMG_SIZE)

                if x_ and y_:  # Ensure non-empty lists before calling min()
                    min_x, min_y = min(x_), min(y_)

                    for i in range(len(hand_landmarks.landmark)):
                        data_aux.append(hand_landmarks.landmark[i].x * IMG_SIZE - min_x)
                        data_aux.append(hand_landmarks.landmark[i].y * IMG_SIZE - min_y)

                    data.append(data_aux)
                    labels.append(dir_)

if data and labels:
    with open('data.pickle', 'wb') as f:
        pickle.dump({'data': data, 'labels': labels}, f)
    print("Dataset successfully saved as data.pickle")
else:
    print("No valid hand landmarks found. Check your images and detection settings.")
