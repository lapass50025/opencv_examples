# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 파일 불러오기
strfile = os.getcwd() + "/datas/images/lena.png"

# OpenCV는 BGR 순서
imgBGR = cv.imread(strfile)
width = imgBGR.shape[1]
height = imgBGR.shape[0]
channel = imgBGR.shape[2]
print("imgBGR type : ", type(imgBGR))
print("imgBGR shape : ", imgBGR.shape)
print("imgBGR, width : {}, height : {}, channel : {}".format(width, height, channel))

# Gray 컬러로 변경하기
imgGray = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)
width = imgGray.shape[1]
height = imgGray.shape[0]
print("imgGray type : ", type(imgGray))
print("imgGray shape : ", imgGray.shape)
print("imgGray, width : {}, height : {}".format(width, height))

# 아래 줄은 오류가 발생함 (imgBGR은 3차원, imgGray는 2차원이라 병합할 수 없음)
# img = np.hstack((imgBGR, imgGray))

# Gray 컬러를 RGB로 변경 후 합치기
imgGrayToBGR = cv.cvtColor(imgGray, cv.COLOR_GRAY2BGR)
img = np.hstack((imgGrayToBGR, imgBGR))

# 출력하기
cv.imshow("TITLE", img)
cv.waitKey(0)

# Gray 크기를 변경 후 합쳐보기
# size=(0, 0) 인 경우 fx, fy 에 배율값을 줌
# fx는 width를 의미하고 0.5인 경우 0.5배 함
# fy는 height를 의미하고 1.0인 경우 1.0배 함
imgGray_resized = cv.resize(imgGray, (0, 0), fx=0.5, fy=1.0, interpolation=cv.INTER_AREA)
imgGrayToBGR = cv.cvtColor(imgGray_resized, cv.COLOR_GRAY2BGR)
img = np.hstack((imgGrayToBGR, imgBGR))

# 출력하기
cv.imshow("TITLE", img)
cv.waitKey(0)

# 이미지 아래에 카메라 영상을 붙여보기
img = cv.imread(strfile)
img_resized = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
camera = cv.VideoCapture(0)

while camera.isOpened():
	result, imgCamera = camera.read()

	if result:
		# 이어 붙이기 위해 크기 맞추기
		width = img_resized.shape[1]
		height = img_resized.shape[1]
		imgCamera_resized = cv.resize(imgCamera, (width, height))

		# 수직으로 이어 붙이기
		imgResult = np.vstack((img_resized, imgCamera_resized))

		# 출력하기
		cv.imshow("TITLE", imgResult)
	else:
		break

	if cv.waitKey(1) == ord('q'):
		break

# 해제하기
if camera.isOpened():
	camera.release()
