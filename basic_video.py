import cv2
cap = cv2.VideoCapture(0)
while True:
    if cv2.waitKey(1) == 13:
        break
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Live Stream", frame)

cap.release()
cv2.destroyAllWindows()