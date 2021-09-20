import cv2

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    cv2.imshow("Camera1", frame1)
    cv2.imshow("Camera1", frame2)
    if cv2.waitKey(10) == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
