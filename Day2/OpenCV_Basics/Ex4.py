import cv2

img = cv2.imread("lena.png")
B,G,R = cv2.split(img)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.imshow("Red Image", R)
cv2.waitKey(0)
cv2.imshow("Green Image", G)
cv2.waitKey(0)
cv2.imshow("Blue Image", B)
cv2.waitKey(0)

merge = cv2.merge([B,G,R+20])
cv2.imshow("Merger", merge)
cv2.waitKey(0)

cv2.destroyAllWindows()