import numpy as np
import cv2 

cap = cv2.VideoCapture('highway1.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# differencce between frame1 and frame2 
diff = cv2.absdiff(frame1, frame2)
cv2.imshow("Absolute Difference", diff)
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
blur = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Blurred", blur)
_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", thresh)
# dilated = cv2.dilate(thresh, None, iterations=1)
# cv2.imshow("Dilation", dilated)
# to find the objects in the Binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)

    if cv2.contourArea(contour) < 500:
        continue
    else:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 3)

# cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
cv2.imshow("Car", frame1)

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release
