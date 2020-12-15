# 외곽선 찾고 도형의 종류 판별하기

# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 불러오기
strfile = os.getcwd() + "/datas/images/shapes.png"
img = cv.imread(strfile)

# gray, thresh 변환하기
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
result, img_thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)

cv.imshow("TITLE", img_thresh)
cv.waitKey(0)

# 외곽선 찾기
contours, hierarchy = cv.findContours(img_thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE )
print("hierachy : ", hierarchy)

# 외곽선이 그려질 빈 영역 생성하기
img_blank = np.copy(img)
img_blank[:] = 255

for contour in contours:
    # 면적 구하기
    area = cv.contourArea(contour)
    print("area : ", area)

    # 그려보기
    color = (255, 0, 0)
    thickness = 1
    cv.drawContours(img_blank, contour, -1, color, thickness)

    # 외곽선 길이 구하기
    peri = cv.arcLength(contour, True)

    # 외곽선 구하기
    epsilon = 0.02 * peri
    approx = cv.approxPolyDP(contour, epsilon, True)

    # 경계 사각형 그리기
    x, y, w, h = cv.boundingRect(approx)

    cv.rectangle(img_blank, (x, y), (x+w, y+h), (0, 255, 0), 2)

    print("shape : ", len(approx))

    # 출력하기
    cv.imshow("TITLE", img_blank)
    cv.waitKey(0)

