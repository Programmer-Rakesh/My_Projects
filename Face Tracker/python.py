import serial
import time
import numpy as np
import cv2

# Initialize serial communication (Change COM port as per your system)
arduinoData = serial.Serial('COM5', 9600)  
time.sleep(2)  # Allow time for connection

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture (0 = internal webcam, 1 = external)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Lower resolution
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)  # Reduce brightness
# Constants for distance calculation (Adjust based on testing)
KNOWN_WIDTH = 14.0  # Approximate width of a human face in cm
FOCAL_LENGTH = 500.0  # Adjust this based on actual camera calibration

def calculate_distance(known_width, focal_length, width_in_frame):
    """Calculate distance based on the apparent width of an object in the frame."""
    if width_in_frame > 0:
        return (known_width * focal_length) / width_in_frame
    return -1  # Return -1 if width is invalid

def send_coordinates_to_arduino(x, y, w, h, distance):
    """Send X, Y coordinates and distance to Arduino via serial."""
    coordinates = f"{x},{y},{distance:.2f}\r"
    arduinoData.write(coordinates.encode())
    print(f"X: {x}, Y: {y}, Z: {distance:.2f} cm")

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 8, minSize=(120, 120))

    for (x, y, w, h) in faces:
        distance = calculate_distance(KNOWN_WIDTH, FOCAL_LENGTH, w)  # Estimate distance
        
        # Draw red rectangle and display X, Y, Z coordinates
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv2.putText(frame, f"X: {x}, Y: {y}, Z: {distance:.2f} cm", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
        # Send data to Arduino
        send_coordinates_to_arduino(x, y, w, h, distance)

    # Resize window and display video
    cv2.namedWindow("Face Tracking", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Face Tracking", 800, 600)
    cv2.imshow("Face Tracking", frame)

    # Press 'd' to exit
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()
arduinoData.close()
