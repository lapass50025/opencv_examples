# 이미지 원근법 변경하기

# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 글자 출력하기
def show_text(imgdata, x, y, strtext):
    font = cv.FONT_HERSHEY_COMPLEX
    scale = 0.5
    color = (0, 255, 255)
    thickness = 1
    cv.putText(imgdata, strtext, (x, y), font, scale, color, thickness)
    cv.imshow("TITLE", imgdata)

# 이미지 불러오기
strfile = os.getcwd() + "/datas/images/cards.jpg"
img_original = cv.imread(strfile)

# 다각형 출력하기
pts = np.array([[111, 219], [287, 188], [352, 440], [154, 482], [111, 219]])
color = (255, 0, 0)
thickness = 2
cv.polylines(img_original, [pts], False, color, thickness)

# 글자 출력하기
show_text(img_original, 111, 219, "111, 219")
show_text(img_original, 287, 188, "287, 188")
show_text(img_original, 352, 440, "352, 440")
show_text(img_original, 154, 482, "154, 482")

cv.imshow("TITLE", img_original)
cv.waitKey(0)

# 이미지 펴보기
height = img_original.shape[0]
width = 250 * height / 340
width = int(width)

# 원근법 좌표 설정하기
pt_src = np.float32([[111,219], [287,188], [154,482], [352,440]])
pt_dest = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(pt_src, pt_dest)

# 원근법이 적용된 이미지 얻기
img_convert = cv.warpPerspective(img_original, matrix, (width, height))

# 수평으로 이어 붙이기
img_result = np.hstack((img_original, img_convert))

# 출력하기
cv.imshow("TITLE", img_result)

cv.waitKey(0)