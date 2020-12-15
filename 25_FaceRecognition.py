# 얼굴 인식하기

# 모듈 불러오기
import cv2 as cv
import numpy as os
import os

# 카메라에서 이미지 읽고 저장하기
def RecordVideo(index):
    result = ()

    # 카메라 객체 얻기
    video = cv.VideoCapture(index)

    count = 0
    save = False
    while video.isOpened():
        # 카메라 읽기
        result, img = video.read()
        cv.imshow("TITLE", img)

        # 저장하기
        if save:
            strfile = os.getcwd() + "/faces/%04d.png" %count
            if result:
                cv.imwrite(strfile, img)
                print(strfile)
            
            # 값 검사하기
            count = count + 1
            if count >= 1000:
                break

        # 키 처리하기
        # s : save
        # p : pause
        # q : quite
        keydata = cv.waitKey(1)
        if keydata == ord('s'):
            save = True
        elif keydata == ord('p'):
            save = False
        elif keydata == ord('q'):
            break
    
    # 해제하기
    if video.isOpened():
        video.release()

# 
if __name__ == "__main__":
    RecordVideo(0)
