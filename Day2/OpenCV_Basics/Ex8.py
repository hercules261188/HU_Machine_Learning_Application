import cv2
import numpy as np

img = np.zeros((512,512,3), dtype="uint8")

def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,0,255),-1)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),50,(0,255,0),-1)

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_circle)

while True:
    cv2.imshow("my_drawing",img)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()