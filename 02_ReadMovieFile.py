# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 동영상 경로 설정하기
strpath = os.getcwd() + "/datas/videos/Armbot.mp4"

# 동영상 파일 열기
cap = cv.VideoCapture(strpath)

# 출력하기
while cap.isOpened():
    # 이미지 읽기
    result, img = cap.read()

    # 출력하기
    if result:
        # 이미지 크기 변경하기
        img_change = cv.resize(img, (640, 480))        

        # 이미지 출력하기
        cv.imshow("TITLE", img_change)
    else:
        break
    
    # 키 검사하기
    keydata = cv.waitKey(1)
    if keydata == ord('q'):
        break

# VideoCapture 해제하기
if cap.isOpened():
    cap.release()
    

    
