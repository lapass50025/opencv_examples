# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 파일 불러오기
strfile = os.getcwd() + "/datas/images/lambo.png"
img = cv.imread(strfile)

# 원본 이미지 정보 출력해보기
print("변수 데이터형 : ", type(img))
print("numpy shape 정보 : ", img.shape)

width = img.shape[1]
height = img.shape[0]
strtitle = "Original Image, width : {}, height : {}".format(width, height)
cv.imshow(strtitle, img)

# 크기 변경해보기
img_resized = cv.resize(img, (1000, 500))
width = img_resized.shape[1]
height = img_resized.shape[0]
strtitle = "Resize Image, width : {}, height : {}".format(width, height)
cv.imshow(strtitle, img_resized)

# 크롭 해보기
# X, Y (행 row, 열 col 순서이므로 세로, 가로 순서)
img_crop = img_resized[200:400, 0:1000]
width = img_crop .shape[1]
height = img_crop .shape[0]
strtitle = "Crop Image, width : {}, height : {}".format(width, height)
cv.imshow(strtitle, img_crop)

cv.waitKey(0)
