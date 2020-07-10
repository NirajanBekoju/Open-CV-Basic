import cv2
import numpy as np

img = cv2.imread('we.jpg')
width = img.shape[0]
height = img.shape[1]

blk = np.zeros(img.shape, np.uint8)
blk[:] = (0, 0, 0)
cv2.imshow("red image", blk)
cv2.rectangle(blk, (0,height-25), (width,height), (255,255,255), cv2.FILLED)

font = cv2.FONT_HERSHEY_SIMPLEX
blk = cv2.putText(blk, 'Nirajan Bekoju', (0,height-10), font, 0.5,(0,0,255), 1, cv2.LINE_AA)
out = cv2.addWeighted(img, 1.0, blk, 0.5, 1)

cv2.imshow('Bio',img)
cv2.imshow('Final', out)
cv2.waitKey(0)
cv2.destroyAllWindows()