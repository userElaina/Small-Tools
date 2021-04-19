import queue
import threading
from time import sleep as slp


def throws(f,args:tuple=tuple())->None:
	if not isinstance(args,tuple):
		args=(args,)
	_t=threading.Thread(target=f,args=args)
	_t.setDaemon(True)
	_t.start()
	return _t

_q=list()
_ed=False

def _f(_n:int=20,_waits:int=0):
	_l=list()
	while True:
		if _ed and len(_q)==0:
			return
		for i in _l.copy():
			if not i.is_alive():
				_l.remove(i)
		while len(_q)>0 and len(_l)<_n:
			f,args=_q.pop(0)
			if not isinstance(args,tuple):
				args=(args,)
			if _waits:
				slp(_waits)
			_l.append(throws(f,args))

_mian=throws(_f)

def restarts(n:int,waits:int=0):
	global _q,_mian,_ed
	_ed=True
	while _mian.is_alive():
		_mian.join()
	_ed=False
	_q=list()
	_mian=throws(_f,(n,waits,))

def throw(f,args:tuple=tuple())->None:
	_q.append((f,args,))

def uq(q,l)->None:
	for i in l:
		q.put(i)


def qthread(l,f,n:int,waits:int=0)->None:
	_threads=[]
	q=queue.Queue(maxsize=n)
	if isinstance(l,int):
		l=list(range(l))
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


rn=0
def f(x,y=1):
	global rn
	rn+=1
	print(x,y)
	slp(3)
	print(x,y+4)


slp(0.3)
restarts(2,0)
slp(0.3)
throw(f,'q1q')
slp(0.3)
throw(f,'q2q')
slp(0.3)
throw(f,'q3q')
slp(0.3)
throw(f,'q4q')
slp(0.3)
throw(f,'q5q')
slp(0.3)
print('qaq')
slp(0.3)
restarts(2,0)
slp(0.3)
print('qwq')
slp(0.3)
throw(f,'q6q')
slp(0.3)
throw(f,'q7q')
slp(0.3)
throw(f,'q8q')
slp(0.3)
throw(f,'q9q')


slp(10000)
