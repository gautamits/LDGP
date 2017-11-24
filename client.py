import cv2
import numpy as np
import scipy
import time
from ldgp import calcgrad
from ldgp import hist
from ldgp import dist

naming=np.load("database/naming.npy")
data=np.load("database/data.npy")
locations=np.load("database/locations.npy")
labels=np.load("database/labels.npy")

face_cascade = cv2.CascadeClassifier('database/haarcascade_frontalface_default.xml')
camera=cv2.VideoCapture(0)
#camera.set(3,240)
#camera.set(4,320)
while True:
	ret,frame=camera.read()
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,2.5,3)
	for (x,y,w,h) in faces:
		face=gray[y: y + h, x: x + w]
        	face=cv2.resize(face,(256,256))
        	gradient=calcgrad(face)
		#gradient=4*gradient
		#gradient=np.array(gradient,dtype='uint8')
        	histogram=hist(gradient)
        	a=[]
        	for i in xrange(len(data)):
            		a.append(dist(data[i], histogram))
            	temp=np.copy(labels)
        	a,temp=zip(*sorted(zip(a,temp)))
        	print a[0],naming[temp[0]]
        	temp=temp[:10]
        	label=np.bincount(temp).argmax()
        	for i in temp:
        		print naming[i]," ",
        	print ""
        	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        	font = cv2.FONT_HERSHEY_SIMPLEX
        	cv2.putText(frame,naming[label],(x,y), font, 0.5,(255,255,255),2)
        	print ""
	cv2.imshow("original",frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
camera.release()
cv2.destroyAllWindows()
