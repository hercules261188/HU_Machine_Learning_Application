import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    B,G,R = cv2.split(img)
    # print(img.shape[:2])
    zeros = np.zeros(img.shape[:2], dtype="uint8")

    cv2.imshow("Real",img)
    cv2.imshow("Red", cv2.merge([zeros,zeros,R]))
    cv2.imshow("Green", cv2.merge([zeros,G,zeros]))
    cv2.imshow("Blue", cv2.merge([B,zeros,zeros]))

    q = cv2.waitKey(10)
    
    if q == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()