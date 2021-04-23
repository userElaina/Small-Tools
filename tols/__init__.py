'''
`pt` `lot` `tm` `trys` `test`

`jsot` `sve` `opens` `openls` `openjs`

`os` `time` `json` `Union`

`sh` `rd` `slp` `cp` `dcp`

`num` `set` `byte` `bytes` `in`

	>>> import os
	>>> import time
	>>> import json
	>>> from typing import Union
	
	>>> from os import system as sh
	>>> from random import choice as rd
	>>> from time import sleep as slp
	>>> from copy import copy as cp
	>>> from copy import deepcopy as dcp

	>>> [num]   int,float,str,
	>>> [set]   list,set,tuple,
	>>> [byte]  bytes,bytearray,memoryview,
	>>> [bytes] str,bytes,bytearray,memoryview,
	>>> [in]    dict,[set],[bytes],

	>>> pt(x)->None
	>>> lot(l:list)->str
	>>> tm(x:float=None,_=False)->str:
	>>> trys(s:all,c:type,default=None)->all
	>>> test(f)->None
	>>> jsot(js:dict,pth=None,indent='\t',onlyascii=False,sort=False,log=False)->str
	>>> sve(pth:str,x:all)->None
	>>> opens(pth:str,s='')->str
	>>> openls(pth:str)->list:
	>>> openjs(pth:str)->dict:
'''

from tols._mian import *

print('import',__name__,'succ')