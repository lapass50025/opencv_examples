# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 디렉터리 경로
strdir = os.getcwd() + "/ImageSave"

# 파일 개수 얻기
files = os.listdir(strdir)
count = len(files)

# VideoWriter 객체 얻기
strfile = strdir + "/001.png"
img = cv.imread(strfile)
height, width, channel = img.shape
stravi = strdir + "/output.avi"

fourcc = cv.VideoWriter_fourcc(*'DIVX')

# tuple 데이터형
size = (width, height)

video = cv.VideoWriter(stravi, fourcc, 0.5, size)

# 저장하기
for i in range(count):
	# 이미지 읽기
	strfile = strdir + "/%03d.png" %i
	img = cv.imread(strfile)

	# 동영셩 파일에 저장하기
	if img is not None:
		cv.imshow("TITLE", img)
		video.write(img)

	cv.waitKey(50)

# 해제하기
cv.destroyAllWindows()
video.release()
cv.waitKey(0)
