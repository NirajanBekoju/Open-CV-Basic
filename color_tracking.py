import cv2
import numpy as np

# image = cv2.imread('hwFellowship.jpg')
video = cv2.VideoCapture('highway.mp4')

while video.isOpened():
    ret, frame = video.read()
    if ret == True:        
        # Conversion of the frame to the HSV Color
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define the range of the blue color
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130, 255, 255])

        # Threshold the image to get only the blue color
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # bitwise and mask and the original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Original Image', frame)
        # cv2.imshow('Masked image', mask)
        cv2.imshow('Result', res)
        if cv2.waitKey(1) == 13:
            break

video.release()
cv2.destroyAllWindows()
