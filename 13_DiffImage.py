# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 카메라의 영상을 시간차를 두고 읽은 후 차이값을 비교해보기

# 변수값 설정하기
scale_value = 1.0

# 카메라 객체 얻기
video = cv.VideoCapture(0)

# 이미지 변환하기
result, imgPrev = video.read()
imgPrev = cv.resize(imgPrev, (0, 0), fx=scale_value, fy=scale_value, interpolation=cv.INTER_AREA)
imgPrev = cv.cvtColor(imgPrev, cv.COLOR_BGR2GRAY)

while video.isOpened():
	# 영상 읽기
	result, img = video.read()

	if not result:
		break

	# 크기 0.5 배로 변경하기
	img = cv.resize(img, (0, 0), fx=scale_value, fy=scale_value, interpolation=cv.INTER_AREA)

	# GRAY 컬러로 변환하기
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

	# 이전 영상과의 차 구하기
	img_diff = cv.absdiff(img, imgPrev)

	# 차이값 개수 구하기
	count = len(img_diff[img_diff > 100])
	print("차이값 개수 : ", count)

	# 출력해보기
	img_result = np.hstack((img, img_diff))
	cv.imshow("TITLE", img_result)

	if cv.waitKey(50) == ord('q'):
		break

	# 이전 영상 변수를 현재 영상으로 갱신하기
	imgPrev = img

# 해제하기
if video.isOpened():
	video.release()

