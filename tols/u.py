'''
`hashname` `smd5` `fmd5` `urlencode` `urldecode`

`HEADERS`

	>>> import re
	>>> import time
	>>> import requests
	>>> from time import sleep as slp
	>>> HEADERS={'User-Agent':Chrome}
	>>> hashname(x:str)->str
	>>> smd5(x:str)->str
	>>> fmd5(pth:str)->str
	>>> urlencode(s:str)->str
	>>> urldecode(s:str)->str
	
'''

import re
import time
import requests
from time import sleep as slp
from tols._u import hashname,smd5,fmd5,HEADERS,urlencode,urldecode

print('import',__name__,'succ')