import cv2
import os

images = os.listdir('images')
print(images)

for img in images:
    image = cv2.imread('images/' + img)
    cv2.imshow(img, image)

cv2.waitKey(0)
cv2.destroyAllWindows()