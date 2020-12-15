# 얼굴 인식하기

# 모듈 불러오기
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

# 카메라에서 이미지 읽고 ./faces 디렉터리에 저장하기
# s : save
# a : add
# p : pause
# q : quite

def RecordVideo(index):
    result = ()

    # 카메라 객체 얻기
    video = cv.VideoCapture(index)

    count = 0
    save = False
    while video.isOpened():
        # 카메라 읽기
        result, img = video.read()

        # 저장하기
        if save and result:
            strfile = os.getcwd() + "/faces/%04d.png" %count
            if result:
                cv.imwrite(strfile, img)
                print(strfile)
            
            # 값 검사하기
            count = count + 1
            if count >= 1000:
                break

        # 키 처리하기
        # s : save
        # p : pause
        # q : quite
        keydata = cv.waitKey(1)
        if keydata == ord('s'):
            save = True
        elif keydata == ord('a'):
            strdir = os.getcwd() + "/faces"
            count = len(os.listdir(strdir))
            save = True
        elif keydata == ord('p'):
            save = False
        elif keydata == ord('q'):
            break
    
    # 해제하기
    if video.isOpened():
        video.release()

# 얼굴 크롭 데이터 얻기
# (x, y, w, h) 튜플 리스트를 리턴함
def GetFrontFaceDetect(img_data):
    result = ()
    # 정면 얼굴 분류 파일 불러오기
    strfile = os.getcwd() + "/datas/haar_cascade_files/haarcascade_frontalface_default.xml"
    cascade = cv.CascadeClassifier(strfile)

    frontfaces = cascade.detectMultiScale(img_data, 1.1, 1)    
    return frontfaces

# 얼굴 이미지 전처리하기
# train, label 데이터 만들기
def MakeTrainAndLabel(list_train, list_label):
    # faces 디렉터리에서 이미지 파일 리스트 만들기
    strdir = os.getcwd() + "/faces"
    files = [file for file in os.listdir(strdir) if os.path.isfile(strdir + "/" + file) ]

    for i, file in enumerate(files):
        strfile = strdir + "/" + file
        img = cv.imread(strfile, cv.IMREAD_GRAYSCALE)

        # 얼굴 크롭 후 학습 데이터 얻기
        faces = GetFrontFaceDetect(img)
        count_face = len(faces)
        if count_face:
            (x, y, w, h) = faces[0]
            img_crop = img[y:y+h, x:x+w]

            # 200 x 200 크기 변경하기
            img_resize = cv.resize(img_crop, (200, 200))

            # 테스트 출력해보기
            if False:
                cv.imshow("TITLE", img_resize)
                cv.waitKey(1)

            list_train.append(img_resize)
            list_label.append(i)

            print("{} 번째".format(i))

# 훈련하기
def TrainFace(list_train, list_label):
    # numpy array로 변환하기
    train_data = np.asarray(list_train)
    label_data = np.asarray(list_label, dtype=np.int32)

    # 모델 생성하기
    model = cv.face.LBPHFaceRecognizer_create()

    # 훈련시키기
    model.train(train_data, label_data)

    return model

# 
if __name__ == "__main__":
    # 저장하기
    RecordVideo(0)

    # 훈련 데이터 전처리하기 (얼굴 크롭, 크기 200x200 변환하기)
    train = list()
    label = list()

    MakeTrainAndLabel(train, label)

    # 훈련하기
    model = TrainFace(train, label)
    
