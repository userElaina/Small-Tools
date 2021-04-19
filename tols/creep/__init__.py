'''
`anime` `stranime` `runoob` `strunoob`

`a2rgb`

	>>> anime(u:str)->list
	>>> stranime(u:str)->str
	>>> runoob(s:str,pl='py3',stdin='')->dict
	>>> strunoob(s:str,pl='py3',stdin='')->str
	>>> a2rgb(rpth:str,wpth:str=None,bg=0xffffff)->None
	>>> tex(s:str,pth:str,api='zhihu',dpi=500,bg:int=None)->str
'''

from tols.creep._anime import anime,stranime
from tols.creep._runoob import runoob,strunoob
from tols.creep._a2rgb import a2rgb
from tols.creep._tex import tex

print('import',__name__,'succ')
