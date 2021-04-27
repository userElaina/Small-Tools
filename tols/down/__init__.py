'''
`throws` `nThread` `nDown`

	>>> throws(f:function,args:tuple)->None
	>>> nThread(
		n:int=20,
		waits:int=0,
		f:function=None,
		args:list=None,
		fast:bool=False
		)
	>>> nDown(
		url:list,
		name:list,
		pth:str,
		h1:list=HEADERS,
		h2:list=HEADERS,
		fu:function=None,
		proxies:dict=None,
		stream_size:int=-1,
		chunk_size:int=1<<20,
		n:int=30,
		waits:int=0,
		print_log:bool=True,
		test7z:bool=False,
		)
'''

from tols.down._thread import throws,nThread
from tols.down._down import nDown

print('import',__name__,'succ')
