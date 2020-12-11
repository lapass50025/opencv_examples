# 모듈 불러오기
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# 이미지 파일 읽기 (548, 342, 3)
strpath = os.getcwd() + "/datas/images/load_image.jpg"

# 이미지 좌표 보기
def show_position():
    img = plt.imread(strpath)
    plt.imshow(img)
    plt.show()

# 글자 출력하기
def show_text(x, y, strtext):
    font = cv.FONT_HERSHEY_COMPLEX
    scale = 0.8
    color = (0, 0, 255)
    thickness = 1
    cv.putText(img, strtext, (x, y), font, scale, color, thickness)
    cv.imshow("TITLE", img)

# opencv에서 이미지 읽기
img = cv.imread(strpath)

# 왼쪽 손 사각형 출력하기
pt1 = (47, 67)
pt2 = (127, 119)
color = (0, 0, 255)
thickness = 2
cv.rectangle(img, pt1, pt2, color, thickness )
cv.imshow("TITLE", img)

# 글자 출력하기
show_text(50, 50, 'Hand')

# 얼굴 원 출력하기
center = (240, 112)
radius = 50
color = (0, 0, 255)
thickness = 2
cv.circle(img, center, radius, color, thickness)

# 글자 출력하기
show_text(240, 50, 'Face')

# 오른쪽 공 사각형 출력하기
pt1 = (327, 270)
pt2 = (400, 337)
color = (0, 0, 255)
thickness = 2
cv.rectangle(img, pt1, pt2, color, thickness )
cv.imshow("TITLE", img)

# 글자 출력하기
show_text(327, 250, 'Ball')

# 발 사각형 출력하기
pt1 = (400, 234)
pt2 = (470, 299)
color = (0, 0, 255)
thickness = 2
cv.rectangle(img, pt1, pt2, color, thickness )
cv.imshow("TITLE", img)

# 글자 출력하기
show_text(400, 210, 'Foot')

cv.waitKey(0)