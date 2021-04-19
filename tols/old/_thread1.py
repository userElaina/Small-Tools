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

print('import',__name__,'succ')
