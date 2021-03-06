import cv2
import numpy as np
import pyautogui

cap=cv2.VideoCapture(0)


blue_lower = np.array([102, 73, 145], np.uint8)
blue_upper = np.array([123, 182, 242], np.uint8)
prev_y=0
while True:
    good,img=cap.read()

    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv_img,blue_lower,blue_upper)
    controus,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for c in controus:
        area=cv2.contourArea(c)
        if area > 500:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            if y < prev_y:
                pyautogui.press('space')

                print('moving down')
            prev_y=y
    cv2.imshow("result", img)




            #cv2.drawContours(img, c, -1, (0, 255, 0), 2)



   # cv2.imshow('mask',mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()