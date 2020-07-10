import numpy as np
import cv2 

cap = cv2.VideoCapture('car.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # find the difference between two images
    diff = cv2.absdiff(frame1, frame2)
    # convert diff matrix into graysclae image
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # apply gaussian blur
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    # Convert inro binary image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=1)
    # cv2.imshow("Dilated", dilated)
    # to find the objects in the Binary image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 2000 or cv2.contourArea(contour) > 30000:
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    cv2.imshow("Car", frame1)
   
    frame1 = frame2
    ret, frame2 = cap.read() 
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release
