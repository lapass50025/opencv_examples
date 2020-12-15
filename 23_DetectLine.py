# 동영상에서 도로 선 감지하기

# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 동영상 파일 불러오기
strfile = os.getcwd() + "/datas/videos/roadway_01.mp4"
video = cv.VideoCapture(strfile)

while video.isOpened():
    # 동영상에서 이미지 읽기
    result, img = video.read()

    if result:
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        result, img_thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

        # 이미지 팽창시켜보기
        kernel = np.ones((15, 15))
        img_dilate = cv.dilate(img_thresh, kernel, iterations=1)

        # 외곽선 찾기
        contours, hierarchy = cv.findContours(img_dilate, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        # 빈 이미지 배열 생성하기
        img_blank = np.copy(img)
        img_blank[:] = 255

        for contour in contours:
            # 면적 구하기
            area = cv.contourArea(contour)
            print("면적 : ", area)

            if area > 10000 and area < 20000:
                # 그리기
                color = (255, 0, 0)
                thickness = 2
                cv.drawContours(img_blank, contour, -1, color, thickness)
                cv.imshow("TITLE", img_blank)

    else:
        # 이미지 위치 변경하기
        video.set(cv.CAP_PROP_POS_MSEC, 0)

    # 키 검사하기
    if cv.waitKey(10) == ord('q'):
        break

# 종료하기
if video.isOpened():
    video.release()
    