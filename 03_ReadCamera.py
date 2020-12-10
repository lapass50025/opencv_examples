# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 카메라 장치 얻기
cap = cv.VideoCapture(0)

# 카메라 너비, 높이 설정하기
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    # 카메라 읽기
    result, img = cap.read()
    
    # 리턴값 검사하기
    if result:
        cv.imshow("TITLE", img)
    
    # 키 읽기
    keydata = cv.waitKey(1)
    if keydata == ord('q'):
        break
    # ESC
    elif keydata == 27:
        break    

# 카메라 해제하기
if cap.isOpened():
    cv.destroyAllWindows()
    cap.release()

