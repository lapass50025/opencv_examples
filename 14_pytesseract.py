# 모듈 불러오기
import cv2 as cv
import pytesseract
from pytesseract import Output
import numpy as np
import os
import sys

# 이미지 데이터 불러오기
strfile = os.getcwd() + "/kor_crop.png"
img = cv.imread(strfile)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# threshold 적용하기
img_threshold = cv.threshold(img_gray, 50, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]

cv.imshow("GRAY", img_gray)
cv.imshow("THRESHOLD", img_threshold)

# 글자 얻기
custom_config = '--oem 3 -l kor+kor_vert+eng --psm 6'
str_result = pytesseract.image_to_string(img_gray, config=custom_config)
print(str_result)

# 글자 좌표 얻기
dict_result = pytesseract.image_to_data(img_gray, config=custom_config, output_type=Output.DICT)

for i, strtext in enumerate(dict_result['text']):
    x = dict_result['left'][i]
    y = dict_result['top'][i]
    width = dict_result['width'][i]
    height = dict_result['height'][i]

    pt1 = (x, y)
    pt2 = (x+width, y+height)
    color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
    cv.rectangle(img, pt1, pt2, color, 2)
    cv.imshow("TITLE", img)
    print(strtext)

cv.waitKey(0)
cv.destroyAllWindows()

