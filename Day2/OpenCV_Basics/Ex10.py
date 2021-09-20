import cv2

def sketch(frame):

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)

    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY)

    return mask

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    cv2.imshow("Original Cam",frame)
    cv2.imshow("Edge Detector",sketch(frame))
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()