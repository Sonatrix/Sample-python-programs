from threading import Thread
import time
def timer(name,delay,repeat):
	while repeat>=0:
		print name+""+repr(time.ctime(time.time()))
		repeat -=  1
	time.sleep(delay)
	print name+"\t"+"completed"
def Main():
	t1=Thread(target = timer,args=('timer1',4,2))
	t2 = Thread(target = timer,args = ('timer2',3,4))

	t1.start()
	t2.start()
	

Main()
