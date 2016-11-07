#! /usr/bin/python

import cv2

for i in range(1,151):
	imgname=str(i)+'.bmp'
	#print imgname
	img=cv2.imread(imgname,cv2.IMREAD_COLOR)
	res=cv2.resize(img,(24,24),interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(imgname,res)
	#cv2.imshow('iker',res)
	#cv2.imshow('image',img)
#cv2.waitKey(0)
#img=cv2.imread('1.bmp',cv2.IMREAD_COLOR);
#res=cv2.resize(img,(24,24),interpolation=cv2.INTER_CUBIC);
#cv2.imshow('image',img);
#cv2.imshow('iker',res);
#cv2.waitKey(0);
