from socket import *
import re
import thread
import sys
import time
import numpy as np

def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def serve(connection,addr,naming,labels,database):
	while True:                                                            
		data=connection.recv(4096)
		data=data.rstrip('\n')
		data=data.rstrip(']')
		data=data.lstrip('[')
		data=np.fromstring(data, dtype=int, sep=' ')
		#data=np.array(data)
		#print data
		a=[]
		for i in xrange(len(database)):
			a.append(dist(data,database[i]))
		temp=np.copy(labels)
		a,temp=zip(*sorted(zip(a,temp)))
		temp=temp[:10]
        	label=np.bincount(temp).argmax()
        	'''for i in temp:
        		print naming[i]," ",
        	print ""
        	'''
		connection.sendall(str(naming[label]))
	connection.close()
	sys.exit()
naming=np.load("data/naming.npy")
database=np.load("data/data.npy")
locations=np.load("data/locations.npy")
labels=np.load("data/labels.npy")
if len(sys.argv) != 3:
	print 'USAGE python server.py <ip> <port>'
	exit(0)
port=int(sys.argv[2])
ip=sys.argv[1]
mysock = socket(AF_INET,SOCK_STREAM)                                                   #start listening on localhost
#mysock.bind(('127.0.0.1',port)) 
mysock.bind((ip,port))  
print 'server running at ',ip,' ',port                                       
mysock.listen(1000)                                                                
while True:
	conn,addr = mysock.accept()
	print 'connected with '+addr[0]+':'+str(addr[1])
	thread.start_new_thread(serve,(conn,addr,naming,labels,database))
	
