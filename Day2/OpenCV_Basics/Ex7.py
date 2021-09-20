import cv2
import numpy as np

img = cv2.imread("lena.png")
height, width = img.shape[:2]

start_row, start_col = int(height*.25), int(width*0.25) 

end_row, end_col = int(height*.75), int(width*0.75) 

crop = img[start_row:end_row, start_col:end_col]

cv2.imshow("Original",img)
cv2.waitKey()
cv2.imshow("Crop",crop)
cv2.waitKey()
cv2.destroyAllWindows()