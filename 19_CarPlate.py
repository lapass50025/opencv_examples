# 모듈 불러오기
import cv2 as cv
import pytesseract
import numpy as np
import os

# 다각형 그리기
def DrawPoloygon(img_data, color, thickness, *pts):
    x = 0
    y = 0

    arr = list()

    # 좌표 리스트 만들기
    for i, pt in enumerate(pts):
        if i % 2 == 0:
            x = pt
        else:
            y = pt
            arr.append([x, y])
    
    # 점 배열 만들기
    arr_pts = np.array([arr])
    cv.polylines(img_data, [arr_pts], False, color, thickness)
    cv.imshow("TITLE", img_data)


# 이미지 불러오기
strfile = os.getcwd() + "/car_plate.jpg"
img = cv.imread(strfile)

# 다각형 그리기
DrawPoloygon(img, (255, 0, 0), 2, 195, 465, 397, 400, 395, 442, 192, 544, 194, 465)

# 출력하기
cv.imshow("TITLE", img)
cv.waitKey(0)

# 깨끗한 이미지 읽기
strfile = os.getcwd() + "/car_plate.jpg"
img = cv.imread(strfile)

# 원근법 이미지 변환하기
width = 400
height = 100
pt_src = np.float32([[195, 465], [397, 400], [192, 544], [395, 442]])
pt_dest = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(pt_src, pt_dest)

# 원근법이 적용된 이미지 얻기
img_convert = cv.warpPerspective(img, matrix, (width, height))

# 출력하기
cv.imshow("TITLE", img_convert)
cv.waitKey(0)

# 원근법 이미지 저장하기
strsave = os.getcwd() + "/car_plate_number.jpg"
cv.imwrite(strsave, img_convert)

# 숫자로 변환하기
custom_config = "-l kor --psm 6 --oem 3"
str_result = pytesseract.image_to_string(img_convert, config=custom_config)
print("번호판 : ", str_result)

# 종료하기
cv.destroyAllWindows()
