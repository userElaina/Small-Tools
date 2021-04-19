import re

_o='/*-+`~!@#$%^&*()_+}{|:"<>?-=[];,./'
_o+=' \t\n\r\v\a\b\f\'\\'
_o+='，。《》？；：‘’“”【】、—（）…￥！~·'
_o+='啊阿'

def clear_ht(x:str)->str:
	return re.sub('^[\s]+','',re.sub('[\s]+$','',x))

def clear_all(x:str)->str:
	for i in _o:
		x=x.replace(i,'')
	return x.lower()

def find_args(x:str)->dict:
	return {i[0]:i[1] 
		for i in [re.sub('[\s]+','',j).split('=') 
			for j in re.findall('[\S]+[\s]*=[\s]*[\S]+',x)]}

def find_para(x:str)->list:
	return re.sub('[\s]+',' ',x).split(' ')
	
print('import',__name__,'succ')