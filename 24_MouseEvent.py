# 마우스 이벤트 처리하기

# 모듈 불러오기
import cv2 as cv
import numpy as np
import os

# 전역 변수
mouse_x = -1
mouse_y = -1
button_status = False

# 마우스 콜백 함수
def mouse_event(event, x, y, flags, param):
    global mouse_x, mouse_y, button_status

    # 왼쪽 마우스 버튼
    if event == cv.EVENT_LBUTTONDOWN:
        button_status = True
        mouse_x = x
        mouse_y = y

    elif event == cv.EVENT_MOUSEMOVE:
        if button_status == True:
            img_copy = np.copy(img)
            cv.rectangle(img_copy, (mouse_x, mouse_y), (x, y), (0, 255, 0), 0)
            cv.imshow("TITLE", img_copy)

    elif event == cv.EVENT_LBUTTONUP:
        button_status = False
        cv.rectangle(img, (mouse_x, mouse_y), (x, y), (0, 255, 0), -1)

# 윈도우 생성하기
cv.namedWindow("TITLE")

# 빈 윈도우 생성하기
img = np.zeros((512, 512, 3))

# 마우스 이벤트 콜백 함수 등록하기
cv.setMouseCallback("TITLE", mouse_event)

while True:
    cv.imshow("TITLE", img)
    if cv.waitKey(10) == ord('q'):
        break

# 해제하기
cv.destroyAllWindows()
