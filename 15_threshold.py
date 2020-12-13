# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 이미지 읽기
strfile = os.getcwd() + "/datas/images/radial_gradient.jpg"
img_original = cv.imread(strfile)

# gray 로 변경하기
img_gray = cv.cvtColor(img_original, cv.COLOR_BGR2GRAY)

# 크기 변경하기
img_original_resized = cv.resize(img_gray , (0, 0), fx=0.5, fy=0.5)

# binary threshold
ret, img_binary = cv.threshold(img_original_resized, 127, 255, cv.THRESH_BINARY)

# binary invert
ret, img_binary_inv = cv.threshold(img_original_resized, 127, 255, cv.THRESH_BINARY_INV)

# trunc
ret, img_trunc = cv.threshold(img_original_resized, 127, 255, cv.THRESH_TRUNC)

# tozero
ret, img_zero = cv.threshold(img_original_resized, 127, 255, cv.THRESH_TOZERO)

# tozero invert
ret, img_zero_inv = cv.threshold(img_original_resized, 127, 255, cv.THRESH_TOZERO_INV)

img_1 = np.hstack((img_original_resized, img_binary, img_binary_inv))
img_2 = np.hstack((img_trunc, img_zero, img_zero_inv))

img_3 = np.vstack((img_1, img_2))

cv.imshow("Original, Binary, Binary Invert, Trunc, ToZero, ToZero Invert", img_3)

cv.waitKey(0)

# 해제하기
cv.destroyAllWindows()
