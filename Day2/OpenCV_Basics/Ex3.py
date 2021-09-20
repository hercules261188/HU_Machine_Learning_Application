import cv2

img = cv2.imread("lena.png")
cv2.imshow("RGB Image",img)
cv2.waitKey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray_img)
cv2.waitKey(0)

ret, img_bin = cv2.threshold(gray_img, 125, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary Image",img_bin)
cv2.waitKey(0)


cv2.destroyAllWindows()