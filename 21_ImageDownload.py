# 모듈 불러오기
import cv2 as cv
import os
import requests
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
			# 이미지 
			image_file = url.split('/')[-1]
			image_name = os.getcwd() + "/download/" + image_file
			
			# 다운로드하기
			result = wget.download(url=url, out=image_name)
			
			i = i + 1
			print("다운로드 파일 : {}, 총 개수 : {}".format(i, total_count))

		except Exception as e:
			print(e)
			
if __name__ == "__main__":
	save_images()
