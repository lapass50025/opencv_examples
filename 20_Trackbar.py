# 모듈 불러오기
import cv2 as cv
import pytesseract
import numpy as np
import os

def nothing():
    pass

# 윈도우 생성하기
cv.namedWindow("Canny Edge")

# 트랙바 생성하기
cv.createTrackbar("low threshold", "Canny Edge", 0, 1000, nothing)
cv.createTrackbar("high threshold", "Canny Edge", 0, 1000, nothing)

# GRAYSCALE 로 읽기
img_gray = cv.imread('datas/images/shapes.png', cv.IMREAD_GRAYSCALE)

while True:
    # 트랙바 값 읽기
    low = cv.getTrackbarPos('low threshold', 'Canny Edge')
    high = cv.getTrackbarPos('high threshold', 'Canny Edge')

    # Canney 이미지 얻기
    img_canny = cv.Canny(img_gray, low, high)

    # 이미지 출력하기
    cv.imshow("Canny Edge", img_canny)

    if cv.waitKey(1) == ord('q'):
        break

