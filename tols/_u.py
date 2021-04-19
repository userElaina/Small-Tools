import os
import re
import time
import requests
from time import sleep as slp
from tols._mian import *
from tols._base import basecode
from tols._hash import hashcode
from tols._other import urlencode,urldecode

HEADERS={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

def hashname(x:str)->str:
	return basecode(int(hashcode(x,'sha224'),16),36,normal=False).zfill(175)

def smd5(x:str)->str:
	return hashcode(x,'md5')

def fmd5(pth:str)->str:
	pth=str(pth)
	return smd5(open(pth,'rb').read())