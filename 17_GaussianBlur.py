# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 불러오기
strfile = os.getcwd() + "/datas/images/lena.png"
img_original = cv.imread(strfile)
img = cv.resize(img_original, (0, 0), fx=0.5, fy=0.5)

# gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# gaussian blur
img_gaussian = cv.GaussianBlur(img_gray, (7, 7), 0)

# canny
img_canny = cv.Canny(img, 150, 255)

# 팽창 연산
kernel = np.ones((5, 5), np.uint8)
img_dilate = cv.dilate(img_canny, kernel, iterations=1)

# 침식 연산
kernel = np.ones((5, 5), np.uint8)
img_erode = cv.erode(img_dilate, kernel, iterations=1)

# 출력하기
img_blank = img_gray.copy()
img_blank[:] = 255
strtitle = "gray, gaussian blur, canny, dilate, erode"
img_1 = np.hstack((img_gray, img_gaussian, img_canny))
img_2 = np.hstack((img_dilate, img_erode, img_blank))

img_3 = np.vstack((img_1, img_2))
cv.imshow(strtitle, img_3)

cv.waitKey(0)
cv.destroyAllWindows()
