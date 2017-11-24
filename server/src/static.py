import sys
import numpy as np
from ldgp import calcgrad
from ldgp import hist
import easygui
def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))
path=easygui.fileopenbox("select the image")
image=cv2.imread(path,0)
image=cv2.resize(image,(240,240))

naming=np.load("database/naming.npy")
labels=np.load("database/labels.npy")
data=np.load("database/data.npy")
grad=calcgrad(image)
histogram=hist(grad)
a=[]
for i in xrange(len(data)):
	a.append(dist(histogram,data[i]))
b=np.copy(a)
temp=np.copy(labels)
temp2=np.copy(labels)
a,temp=zip(*sorted(zip(a,temp)))
b,locations=zip(*sorted(zip(b,temp2)))
for i in xrange(10):
	
	
