import cv2
import numpy as np

def hsvChange(a):
    pass

# Making of the trackbar windows HSV
cv2.namedWindow("HSV Trackbar - Color Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("HSV Trackbar - Color Detection", 640, 240)
cv2.createTrackbar("Min Hue", "HSV Trackbar - Color Detection", 0, 180, hsvChange)
cv2.createTrackbar("Max Hue", "HSV Trackbar - Color Detection", 180, 180, hsvChange)
cv2.createTrackbar("Min Saturation", "HSV Trackbar - Color Detection", 0, 255, hsvChange)
cv2.createTrackbar("Max Saturation", "HSV Trackbar - Color Detection", 255, 255, hsvChange)
cv2.createTrackbar("Min Value", "HSV Trackbar - Color Detection", 0, 255, hsvChange)
cv2.createTrackbar("Max Value", "HSV Trackbar - Color Detection", 255, 255, hsvChange)

image = cv2.imread('paper.jpg')
image = cv2.resize(image, None, fx = 0.5, fy = 0.5)
cv2.imshow("Original",image)

while True:
    h_min = cv2.getTrackbarPos("Min Hue", "HSV Trackbar - Color Detection")
    h_max = cv2.getTrackbarPos("Max Hue", "HSV Trackbar - Color Detection")
    s_min = cv2.getTrackbarPos("Min Saturation", "HSV Trackbar - Color Detection")
    s_max = cv2.getTrackbarPos("Max Saturation", "HSV Trackbar - Color Detection")
    v_min = cv2.getTrackbarPos("Min Value", "HSV Trackbar - Color Detection")
    v_max = cv2.getTrackbarPos("Max Value", "HSV Trackbar - Color Detection")
    
    lower = np.array([h_min, s_min, v_min])
    higher = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(image, lower, higher)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
