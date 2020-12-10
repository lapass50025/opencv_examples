# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 경로 설정하기
strpath = os.getcwd() + "/datas/images/lena.png"

# 이미지 읽기
img = cv.imread(strpath)

# 이미지 정보 확인하기
print("type : ", type(img))
print("shape : ", img.shape)
print("dtype : ", img.dtype)

# 이미지 출력하기
cv.imshow("Title", img)
cv.waitKey(0)
