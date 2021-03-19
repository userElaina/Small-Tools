import requests

from tols._mian import *
from tols._code import hashcode,basecode

def hashname(x:str)->str:
	return basecode(int(hashcode(x,'sha224'),16),36,normal=False).zfill(175)

def smd5(x:str)->str:
	return hashcode(x,'md5')

def fmd5(pth:str)->str:
	pth=str(pth)
	return smd5(open(pth,'rb').read())