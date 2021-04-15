import queue
import threading

from tols._mian import *

def uq(q,l:set_type)->None:
	for i in l:
		q.put(i)

def throws(f,args:tuple=tuple())->None:
	_t=threading.Thread(target=f,args=args)
	_t.setDaemon(True)
	_t.start()
	return _t

def qthread(l:set_type,f,n:int,waits:int=0)->None:
	_threads=[]
	q=queue.Queue(maxsize=n)
	throws(uq,args=(q,l,))
	while q.qsize()>0:
		while len(_threads)>=n:
			for i in _threads.copy():
				if not i.is_alive():
					_threads.remove(i)
		args=q.get()
		if not isinstance(args,tuple):
			args=(args,)
		if waits:
			slp(waits)
		_threads.append(throws(f,args))
	for i in _threads:
		i.join()

_showthread_n=0
def _showthread(x=6):
	global _showthread_n
	_showthread_n+=1
	tn=_showthread_n
	for i in range(x):
		msg=str(i)+' seconds after n='+str(tn)+', but now n='+str(_showthread_n)
		print(msg)
		slp(1)

def _test_f(x):
	x=trys(int,x,6)
	t=threading.Thread(target=_showthread,args=(x,))
	t.start()

print('import',__name__,'succ')
