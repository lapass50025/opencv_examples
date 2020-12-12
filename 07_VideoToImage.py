# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 저장 경로
strpath = os.getcwd() + "/ImageSave"

# 디렉터리 생성하기
def MakeSaveDir():
    bDir = os.path.exists(strpath)
    if not bDir:
        os.mkdir(strpath)

# Video 파일 불러오기
def LoadVideo():
    strfile = os.getcwd() + "/datas/videos/Armbot.mp4"
    cap = cv.VideoCapture(strfile)
    return cap

# Video To Image 저장하기
def SaveVideoToImage(cap, img):
    if cap.isOpened():
        result, img = cap.read()
    
    if result:
        dirobj = os.listdir(strpath)
        count = len(dirobj)
        strfile = strpath + "/%03d.png" %count
        cv.imwrite(strfile, img)

def main():
    # 디렉터리 생성하기
    MakeSaveDir()

    # 동영상 파일 불러오기
    pos = 0
    cap = LoadVideo()
    while cap.isOpened():
        # 동영상 위치 변경하기
        cap.set(cv.CAP_PROP_POS_MSEC, pos)

        # 500 ms 단위로 저장하기
        pos = pos + 500

        # 영상 읽기
        result, img = cap.read()

        # 이미지 저장하기
        if result:
            SaveVideoToImage(cap, img)
        else:
            break

    # 해제하기
    if cap.isOpened():
        cap.release()

if __name__ == "__main__":
    main()


