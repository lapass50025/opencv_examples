# 모듈 불러오기
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# 이미지 파일 불러오기
strfile = os.getcwd() + "/datas/images/sudoku.jpg"
img = cv.imread(strfile, cv.IMREAD_GRAYSCALE)

# threshold binary
result, img_threshold = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# adaptive threshold by mean
img_mean = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 4)

# adaptive threshold by gaussian
img_gaussian = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 4)

# 출력하기

# 원본 파일
plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')

# threshold binary
plt.subplot(1, 4, 2)
plt.imshow(img_threshold, cmap='gray')

# adaptive threshold by mean
plt.subplot(1, 4, 3)
plt.imshow(img_mean, cmap='gray')

# adaptive threshold by gaussian
plt.subplot(1, 4, 4)
plt.imshow(img_gaussian, cmap='gray')

plt.show()