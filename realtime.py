import cv2
import numpy as np
from ldgp import *
camera=cv2.VideoCapture(0)

while True:
	ret,frame=camera.read()
	r,c=frame.shape[:2]
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gradient=calcgrad(gray)
	#gradient=4*gradient
	new_frame=np.zeros((r,c*2,3))
	new_frame[:,0:c,:]=frame
	gradient=cv2.cvtColor(gradient,cv2.COLOR_GRAY2RGB)
	new_frame[:,c:c*2+1]=gradient
	new_frame=np.array(new_frame,dtype='uint8')
	#gradient=np.array(gradient,dtype='uint8')
	#laplacian = cv2.Laplacian(gray,cv2.CV_64F)
	#cv2.imshow("original",frame)
	cv2.imshow("ldgp",new_frame)
	#cv2.imshow("laplacian",laplacian)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
camera.release()
cv2.destroyAllWindows()



