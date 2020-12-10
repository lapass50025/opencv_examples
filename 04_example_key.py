# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 기능 정의하기
# q : end
# i : image
# v : video
# w : webcam

# 빈 이미지 보기
def show_blank():
    # 빈 윈도우 생성하기
    data = np.zeros((640, 480, 3))
    data[:] = 255
    cv.imshow("TITLE", data)

# 이미지 보기
def show_image():
    # 이미지 파일 경로 설정하기
    strpath = os.getcwd() + "/datas/images/lena.png"

    # 이미지 읽기
    img = cv.imread(strpath)
    
    # 이미지 출력하기
    cv.imshow("TITLE", img)

    # 대기하기
    cv.waitKey(0)
    show_blank()

# 동영상 보기
def show_movie():
    # 동영상 경로 설정하기
    strpath = os.getcwd() + "/datas/videos/Armbot.mp4"

    # 동영상 파일 열기
    cap = cv.VideoCapture(strpath)

    while cap.isOpened():
        # 동영상 읽기
        result, img = cap.read()

        if result:
            # 이미지 크기 변경하기
            img_changed = cv.resize(img, (640, 480))

            # 출력하기
            cv.imshow("TITLE", img_changed)
        
        else:
            # 동영상 다시 읽기
            cap.set(cv.CAP_PROP_POS_MSEC, 0)
        
        # 키 검사하기
        keydata = cv.waitKey(10)
        if keydata == ord('q'):
            break

    # 종료하기
    if cap.isOpened():
        cap.release()
    
    show_blank()

# 웹캠 출력하기
def show_camera():
    # 카메라 장치 얻기
    cap = cv.VideoCapture(0)

    # 출력하기
    while cap.isOpened():
        # 카메라 읽기
        result, img = cap.read()

        # 카메라 검사하기
        if result:
            # 이미지 크기 변경하기
            img_changed = cv.resize(img, (640, 480))

            # 이미지 출력하기
            cv.imshow('TITLE', img_changed)
        else:
            break
        
        # 키 처리하기
        keydata = cv.waitKey(1)
        if keydata == ord('q'):
            break
    
    # 종료하기
    if cap.isOpened():
        cap.release()
    
    show_blank()

while True:
    # 키 입력받기
    show_blank()
    keydata = cv.waitKey(1)

    # 종료하기
    if keydata == ord('q'):
        break

    # 이미지 출력하기
    elif keydata == ord('i'):
        show_image()
    
    # 동영상 파일 출력하기
    elif keydata == ord('v'):
        show_movie()        

    # 웹캠 출력하기
    elif keydata == ord('w'):
        show_camera()

# 종료하기
cv.destroyAllWindows()
