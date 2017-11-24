import cv2
import numpy as np
import scipy
import time
import socket
import sys
from ldgp import calcgrad
from ldgp import hist

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera=cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print s

#ret=s.connect(("localhost",8001))
if len(sys.argv) != 3:
	print "USAGE python client1.py <ip of server> <port of server>"
ip=sys.argv[1]
port=int(sys.argv[2])
ret=s.connect((ip,port))
#print ret
while True:
	ret,frame=camera.read()
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,2.5,3)
	for (x,y,w,h) in faces:
		face=gray[y: y + h, x: x + w]
        	face=cv2.resize(face,(240,240))
        	gradient=calcgrad(face)
		#gradient=4*gradient
		#gradient=np.array(gradient,dtype='uint8')
        	histogram=hist(gradient)
        	histogram=str(histogram)
        	print 'histogram', histogram
        	s.sendall(histogram)
        	print 'histogram sent'
        	name=s.recv(4096)
        	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        	font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(frame,naming[labels[0]],(x,y), font, 0.5,(255,255,255),2,cv2.LINE_AA)
        	cv2.putText(frame,name,(x,y), font, 0.5,(255,255,255),2,cv2.LINE_AA)
        	print ""
	cv2.imshow("original",frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
camera.release()
cv2.destroyAllWindows()
