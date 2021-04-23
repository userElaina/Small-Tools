# import os
# import time
# from os import system as sh
import requests
from tols.downs._thread import *

HEADERS={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

gh=lambda u,px,h:requests.head(u,proxies=px,headers=h) if px else requests.head(u,headers=h)
gt=lambda u,px,h:requests.get(u,proxies=px,headers=h) if px else requests.get(u,headers=h)
gts=lambda u,px,h:requests.get(u,proxies=px,headers=h,stream=True) if px else requests.get(u,headers=h,stream=True)


class nDown:
	def __init__(
		self,
		url:list,
		name:list,
		pth:str,
		proxies:dict=None,
		h1:list=HEADERS,
		h2:list=HEADERS,
		fu=None,
		stream_size:int=-1,
		chunk_size:int=1<<20,
		n:int=30,
		waits:int=0,
		print_log:bool=True,
		test7z:bool=False,
	):
		if isinstance(url,str):
			url=[url,]
		self.url=list(url).copy()
		self.u2=list(url).copy()

		self.le=len(self.url)
		self.size=[-1,]*self.le
		# self.time=self.size.copy()
		# self.code=self.size.copy()

		if isinstance(name,str):
			name=[name+str(i) for i in range(self.le)]
		self.name=list(name).copy()

		self.pth=pth
		self.h1=h1
		self.h2=h2
		self.fu=fu
		self.proxies=proxies
		self.stream_size=stream_size
		self.chunk_size=chunk_size
		self.print_log=print_log
		self.test7z=test7z

		exist=list(os.walk(pth))[0][-1]
		self.l=[i for i in range(self.le) if (self.name[i] not in exist and self.name[i]+'.sve_def' not in exist)]
		# self.l=[i for i in range(self.le) if self.name[i] not in exist]
		self.__pt(len(self.l))
		self.__mian=nThread(n=n,waits=waits)
	
	def __pt(self,*args):
		if not self.print_log:
			return 
		print(*args)

	def __get_f(
		self,
		i:int,
		h:dict,
	)->float:
		url=self.u2[i]
		a=float(time.time())
		
		name=self.pth+self.name[i]
		if self.size[i]>=self.stream_size:
			nm=name+'.pyd_def'
			if os.path.exists(nm):
				tsz=os.path.getsize(nm)
				h['Range']='bytes='+str(tsz)+'-'
				self.__pt(i,'from',tsz>>20,'to',self.size[i]>>20)
			else:
				self.__pt(i,'from -1 to',self.size[i]>>20)
			res=gts(url,self.proxies,h)
			with open(nm,'ab') as f:
				for chunk in res.iter_content(chunk_size=self.chunk_size):
					if chunk:
						f.write(chunk)
						f.flush()
			od='move "'+nm+'" "'+name+'"'
			sh(od)
		else:
			res=gt(url,self.proxies,h)
			open(name,'wb').write(res.content)
		if self.test7z:
			od='7z t "'+name+'"'
			odd=('move "'+name+'" "'+name+'.err_def"') if sh(od) else ('echo \'\' > "'+name+'.sve_def"')
			sh(odd)

		return float(time.time())-a

	def __d1(self,i:int,)->int:
		url=self.url[i]
		name=self
		url=self.fu(url,name) if self.fu else url
		
		if isinstance(self.h1,list):
			h1=self.h1[i]
		else:
			h1=self.h1

		if isinstance(self.h2,list):
			h2=self.h2[i]
		else:
			h2=self.h2

		
		if isinstance(h1,dict):
			h=h1
		else:
			h=h1(url,name)

		try:
			res=requests.head(url,proxies=self.proxies,headers=h)
			# self.__pt(url)
			codes=int(res.status_code)
		except:
			codes=-1

		self.__pt(i,'1st get',codes)

		if codes==302:
			self.u2[i]=res.headers['Location']
			try:
				if not isinstance(h2,dict):
					h=h2(url,name,h.copy())
				res=requests.head(self.u2[i],proxies=self.proxies,headers=h)
				codes=int(res.status_code)
			except:
				codes=-1
			self.__pt(i,'2nd get',codes)

		try:
			self.size[i]=int(res.headers['Content-Length'])
		except:
			self.size[i]=0

		_time=self.__get_f(i,h.copy())
		self.__pt(i,'used',_time,'toget',self.size[i]>>20)

		return codes

	def starts(self):
		self.__mian.ths(self.__d1,self.l)
	
	def join(self):
		self.__mian.join()

print('import',__name__,'succ')
