# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 정면 얼굴 분류 파일 불러오기
strfile = os.getcwd() + "/datas/haar_cascade_files/haarcascade_frontalface_default.xml"
cascade = cv.CascadeClassifier(strfile)

# 눈 분류 파일 불러오기
strfile = os.getcwd() + "/datas/haar_cascade_files/haarcascade_eye.xml"
cascadeEye = cv.CascadeClassifier(strfile)

# 코 분류 파일 불러오기
strfile = os.getcwd() + "/datas/haar_cascade_files/haarcascade_mcs_nose.xml"
cascadeNose = cv.CascadeClassifier(strfile)

# 이미지 파일 불러오기

# strimg = os.getcwd() + "/datas/images/lena.png"
strimg = os.getcwd() + "/datas/images/faces.jpg"
# strimg = os.getcwd() + "/datas/images/people.jpg"
img = cv.imread(strimg)

# 검색하기
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# scale factor : 1.1
# min neighbor : 1
frontfaces = cascade.detectMultiScale(imgGray, 1.1, 1)

# 사각형 그리기
for (x, y, w, h) in frontfaces:
	cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)

# scale factor : 1.1
# min neighbor : 15
eye = cascadeEye.detectMultiScale(imgGray, 1.1, 15)

# 사각형 그리기
for (x, y, w, h) in eye:
	cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

# scale factor : 1.1
# min neighbor : 30
nose = cascadeNose.detectMultiScale(imgGray, 1.1, 30)

# 사각형 그리기
for (x, y, w, h) in nose:
	cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5)

# 출력하기
img_resized = cv.resize(img, (0,0), fx=0.5, fy=0.5)
cv.imshow("TITLE", img_resized)


cv.waitKey(0)
cv.destroyAllWindows()
