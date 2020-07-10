import cv2
img = cv2.imread('we.jpg')
cv2.imshow('Original', img)
cv2.imshow('Scalar', 0.5 * img)
