import cv2

img = cv2.imread("cute.jpg", 1)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.4) 

img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('nati23456.jpg', img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




