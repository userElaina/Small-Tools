import queue
import threading
# from time import sleep as slp
from tols._mian import *

def throws(f,args:tuple=tuple())->None:
	if not isinstance(args,tuple):
		args=(args,)
	_t=threading.Thread(target=f,args=args)
	_t.setDaemon(True)
	_t.start()
	return _t

class nThread:
	def __init__(
		self,
		n:int=20,
		waits:int=0,
		f=None,
		args:list=None,
		fast:bool=False
	):
		self.__ed=False
		self.__q=list()
		self.__n=n
		self.__waits=waits
		self.__mian=throws(self.__f)
		if fast:
			self.ths(f,args)
			self.join()


	def __repr__(self):
		return '<class qThread with '+str(self.__n)+' threads and '+str(self.__waits)+' seconds wait time>'

	# def __del__(self):
	# 	print('del this qThread, but '+str(self.__n)+'(or less) threads are running...')

	def __f(self):
		_l=list()
		while True:
			if self.__ed and not len(_l):
				return
			for i in _l.copy():
				if not i.is_alive():
					_l.remove(i)
			while len(self.__q)>0 and len(_l)<self.__n:
				f,args=self.__q.pop(0)
				if not isinstance(args,tuple):
					args=(args,)
				if self.__waits:
					slp(self.__waits)
				_l.append(throws(f,args))
	
	def th(self,f,args:tuple=tuple()):
		self.__q.append((f,args,))

	def thl(self,args:list):
		self.__q+=args

	def ths(self,f,args:list):
		if isinstance(args,int):
			args=list(range(args))
		self.__q+=[(f,i,) for i in args]

	def join(self):
		self.__ed=True
		self.__mian.join()
		self.__ed=False

print('import',__name__,'succ')
