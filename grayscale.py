import cv2
img = cv2.imread('bio.jpg')
cv2.imshow('Nirajan', img)
# print("Shape: ", img.shape)
# print("Height pixel Value : ", img.shape[0])
cv2.waitKey(0)
# Grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_img)
cv2.imwrite('grayscale.png', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()