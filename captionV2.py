import cv2
import numpy as np

img = cv2.imread('bio.jpg')
height = img.shape[0]
width = img.shape[1]
print(width, height)
cv2.imshow("Original", img)
cv2.rectangle(img, (0,height-25), (width, height), (0,0,0), cv2.FILLED)

cv2.imshow("Rectangle", img)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Photo By : Nirajan Bekoju', (0,height-10), font, 0.5,(255,255,255), 1, cv2.LINE_AA)

cv2.imshow("Finale", img)
cv2.imwrite('caption.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()