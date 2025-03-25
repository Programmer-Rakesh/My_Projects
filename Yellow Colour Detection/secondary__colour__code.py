import cv2
import numpy as np


def get_limits(color):
    # Convert single color value to a 1x1 image
    color = np.uint8([[color]])

    # Now convert to HSV
    hsvC = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    lowerLimit = np.array([hsvC[0][0][0] - 10, 100, 100])
    upperLimit = np.array([hsvC[0][0][0] + 10, 255, 255])

    return lowerLimit, upperLimit