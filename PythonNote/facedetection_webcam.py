# -*- coding: utf-8 -*-
from VideoCapture import Device
import time
import sys, pygame
import cv

if __name__ == "__main__":
	hc = cv.Load("E:\\Software\\Notepad++\\PythonEnv\\haarcascade_frontalface_alt.xml")
	
	while True:
		pygame.init()
		pygame.display.set_caption('FaceDetection') 
		screen = pygame.display.set_mode([620,485])
		
		#��ʼ������ͷ
		cam = Device(devnum=0, showVideoWindow=0)

		#ץͼ
		cam.saveSnapshot('temp.jpg', timestamp=3, boldfont=1, quality=80)
		#����ʶ��
		image=cv.LoadImage('temp.jpg', cv.CV_LOAD_IMAGE_COLOR)
		face = cv.HaarDetectObjects(image, hc, cv.CreateMemStorage(), 1.2,2, cv.CV_HAAR_DO_CANNY_PRUNING, (0,0) )
		for (x,y,w,h),n in face:
			# print("[(%d,%d) -> (%d,%d)]" % (x,y,x+w, y+h))
			cv.Rectangle(image,(int(x),int(y)),(int(x)+w,int(y)+h),(255,255,255),1,0)
		cv.SaveImage('temp_detec.jpg', image)
		
		#����ͼ��
		image = pygame.image.load('temp_detec.jpg')
		#���ͻ���
		screen.blit(image,[2, 2])

		#��ʾͼ��
		pygame.display.flip()
		
		time.sleep(0.1)