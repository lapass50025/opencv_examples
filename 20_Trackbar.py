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
strfile = os.getcwd() + "/datas/images/shapes.png"
img = cv.imread(strfile)
img_resized = cv.resize(img, (0,0), fx=0.5, fy=0.5)

img_gray = cv.imread('datas/images/shapes.png', cv.IMREAD_GRAYSCALE)
img_gray_resized = cv.resize(img_gray, (0, 0), fx=0.5, fy=0.5)

while True:
    # 트랙바 값 읽기
    low = cv.getTrackbarPos('low threshold', 'Canny Edge')
    high = cv.getTrackbarPos('high threshold', 'Canny Edge')

    # Canney 이미지 얻기
    img_canny = cv.Canny(img_gray_resized, low, high)

    # 이미지 수평으로 합치기
    img_canny_bgr = cv.cvtColor(img_canny, cv.COLOR_GRAY2BGR)
    img_sum = np.hstack((img_resized, img_canny_bgr))

    # 이미지 출력하기
    cv.imshow("Canny Edge", img_sum)

    if cv.waitKey(1) == ord('q'):
        break

