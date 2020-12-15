# 모듈 불러오기
import cv2 as cv
import os
import requests
from urllib import parse
import wget
from PIL import Image
import time
import requests # to get image from the web
import shutil # to save it locally


strurl = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02114548"

def download_image(image_url):
    filename = "download/" + image_url.split("/")[-1]

    r = requests.get(image_url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

def save_images():
    # URL 열기
    res = requests.get(strurl)
    
    # 데이터 읽기
    strtext = res.content.decode("utf-8")
    
    # 파싱하기
    url_list = strtext.split('\r\n')
    
    i = 0
    total_count = len(url_list)
    
    # 다운로드하기
    for url in url_list:
        try:
            download_image(url)

            i = i + 1
            print("다운로드 파일 : {}, 총 개수 : {}".format(i, total_count))
                        
        except Exception as e:
            total_count = total_count - 1
            print(e)
            
if __name__ == "__main__":
    save_images()
