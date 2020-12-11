# 모듈 불러오기
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 3차원 512 x 512 x 3 매트릭스 만들기
img = np.zeros((512, 512, 3), np.uint8)

# OpenCV는 BGR (Blue, Green, Red)
img[:] = 255, 0, 0


# cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv.rectangle(img,(0,0),(250,350),(0,0,255),2)
# cv.imshow("Image",img)

# cv.circle(img,(400,50),30,(255,255,0),5)

# cv.imshow("Image",img)

# cv.waitKey(0)
# cv.destroyAllWindows()


# 선 그리기
x1 = 0
y1 = 0
x2 = img.shape[0]
y2 = img.shape[1]
color = (0, 0, 255)
thickness = 3

cv.line(img, (x1, y1), (x2, y2), (color), thickness)

# 사각형 그리기
x1 = 10
y1 = 10
x2 = 502
y2 = 40
color = (0, 255, 0)
thickness = 5
cv.rectangle(img,(x1, y1),(x2, y2), color, thickness)

# 원 그리기
x = img.shape[0] // 2
y = img.shape[1] // 2
radius = 30
color = (0, 255, 0)
thickness = 2
cv.circle(img, (x, y), radius, color, 2)

# 텍스트 출력하기
strtext = "Hello, World!!!"
x = 100
y = 200
font = cv.FONT_HERSHEY_COMPLEX
scale = 1
color = (0, 150, 0)
thickness = 3
cv.putText(img, strtext, (x, y), font, scale, color, thickness)

# 이미지 출력하기
cv.imshow("TITLE", img)

cv.waitKey(0)

