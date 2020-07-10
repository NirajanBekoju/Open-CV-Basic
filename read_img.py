import cv2
img = cv2.imread('bio.jpg')
cv2.imshow('Nirajan', img)
print("Shape: ", img.shape)
print("Height pixel Value : ", img.shape[0])
cv2.waitKey(0)
cv2.destroyAllWindows()