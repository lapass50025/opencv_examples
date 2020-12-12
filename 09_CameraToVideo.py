# 모듈 불러오기
import cv2 as cv
import numpy as np
import os


# 변수 설정하기
width = 640
height = 480
fps = 10

# VideoCapture 객체 생성하기
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FPS, fps)

# VideoWriter 객체 생성하기
# 코덱 설정하기
fourcc = cv.VideoWriter_fourcc(*'XVID')
video = cv.VideoWriter('./output.avi', fourcc, fps, (width, height))

while True:
	# 카메라에서 읽기
	result, img = cap.read()

	# 저장하기
	if result:
		video.write(img)
		cv.imshow('TITLE', img)

	if cv.waitKey(1) == ord('q'):
		break

# 해제하기
if cap.isOpened():
	cap.release()

if video.isOpened():
	video.release()
