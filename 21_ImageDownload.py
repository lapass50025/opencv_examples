# 모듈 불러오기
import cv2 as cv
import os
import requests
from urllib import parse
import wget

strurl = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02114548"

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
            if url.find("%20") == -1:
                # 이미지 
                image_file = url.split('/')[-1]
                image_file.replace(' ', '')
                image_name = os.getcwd() + "/download/" + image_file
                image_name = parse.unquote(image_name)
                
                # 다운로드하기
                print("url : ", url, "file : ", image_file)
                os.system("curl --connect-timeout 10 --max-time 10 " + url + " -o " + image_name)
                
                i = i + 1
                print("다운로드 파일 : {}, 총 개수 : {}".format(i, total_count))
            else:
                total_count = total_count - 1
                
        except Exception as e:
            total_count = total_count - 1
            print(e)
            
if __name__ == "__main__":
    save_images()
