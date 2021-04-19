'''
`throws` `nThread` `nDown`

	>>> throws(f,args:tuple)->None
	>>> nThread(
		self,
		n:int=20,
		waits:int=0,
		f=None,
		args:list=None,
		fast:bool=False
		)
	>>> nDown(
		url:list,
		name:list,
		pth:str,
		h1:list=HEADERS,
		h2:list=HEADERS,
		fu=None,
		stream_size:int=-1,
		chunk_size:int=1<<20,
		n:int=30,
		waits:int=0,
		print_log:bool=True,
		)
'''

from tols.downs._thread import throws,nThread
from tols.downs._down import nDown

print('import',__name__,'succ')
