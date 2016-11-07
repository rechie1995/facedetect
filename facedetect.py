#! /usr/bin/env python

import numpy as np
import cv2
import cv2.cv as cv
#from video import create_capture
from common import clock, draw_str

help_message = '''In fact I don't konw why.'''

def detect(img,cascade):
	rects = cascade.detectMultiScale(img,scaleFactor=1.3,minNeighbors=4,minSize=(30,30),flags = cv.CV_HAAR_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

def draw_rects(img,rects,color):
	for x1,y1,x2,y2 in rects:
		cv2.rectangle(img,(x1,y1),(x2,y2),color,2)

if __name__ == '__main__':
	import sys,getopt
	print help_message

	args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade='])
	try: video_src = video_src[0]
	except: video_src = 0
	args = dict(args)
	cascade_fn = args.get('--cascade', "xml.xml")
	#cascade_fn = args.get('--cascade', "/home/rechie/opencv-2.4.13/data/haarcascades/haarcascade_frontalface_alt.xml")	
	cascade = cv2.CascadeClassifier(cascade_fn)

	cam = cv2.VideoCapture("/home/rechie/Videos/4.avi")

	while True:
		ret, img = cam.read()
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)

		t = clock()
		rects = detect(gray,cascade)
		vis = img.copy()
		draw_rects(vis, rects, (0, 255, 0))
		#for x1, y1, x2, y2 in rects:
			#roi = gray[y1:y2, x1:x2]
			#vis_roi = vis[y1:y2, x1:x2]
			#subrects = detect(roi.copy(),nested)
			#draw_rects(vis_roi, subrects, (255, 0, 0))
		dt = clock() - t

		draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
		cv2.imshow('facedetect', vis)
		
		if 0xFF & cv2.waitKey(5) == 27:
			break
	cv2.destroyAllWindows()
