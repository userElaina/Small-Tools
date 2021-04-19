from tols._u import *

INT_MAX=2147483648
_int=lambda x:x if -INT_MAX<=x<=INT_MAX-1 else (x+INT_MAX)%(2*INT_MAX)-INT_MAX
_asc2=lambda a:a.encode('gbk')

# def _int(x):return x if -INT_MAX<=x<=INT_MAX-1 else (x+INT_MAX)%(2*INT_MAX)-INT_MAX
# def ans2(a):return a.encode('gbk')

def kr(a,b):
	c=0
	b=_asc2(b)
	while c < len(b)-2:
		d=b[c+2]
		d=d-87 if _asc2('a')[0]<=d else int(chr(d))
		d=a>>d if _asc2('+')[0]==b[c+1] else a<<d
		d=_int(d)
		a=a+d&4294967295 if _asc2('+')[0]==b[c] else a^d
		c+=3
	return _int(a)

def mr(q,tkk):
	e=q.encode()
	d=str(tkk).split('.')
	a=int(d[0])
	b=int(d[0])
	for f in e:
		a+=f
		a=kr(a,'+-a^+6')
	a=kr(a,'+-3^+b+-f')
	a&=0xffffffff
	a^=(int(d[1]) or 0)
	if 0>a:
		a=(a&(INT_MAX-1))+INT_MAX
	a%=1E6
	a=int(a)
	return (str(a)+'.' +str(a^b))

headers={
	'Referer':'https://translate.google.cn/',
	'Host':'translate.google.cn'
}
url='https://translate.google.cn/translate_a/single'

def trans(q:str,r:str,w:str,tkk:str='426151.3141811846')->dict:
	'MAX:5000(utf-8)'
	tk=mr(q,tkk)
	params={
		'client':'t',
		'sl':r,
		'tl':w,
		'hl':r,
		'dt':['at','qca','rw','rm','ss','t'],
		'tk':tk,
		'ie':'UTF-8',
		'oe':'UTF-8',
		'pc':1,
		'kc':1,
		'ssel':0,
		'otf':1
	}
	data={
		'q':q
	}
	resp=requests.post(url,params=params,data=data,headers=headers)
	if resp.status_code==200:
		resp.encoding='utf-8'
		return resp.json()
	else:
		return None

def js2ms(ms=None)->str:
	if ms==None or ms=='':
		return ''
	return ''.join(map(lambda x:x[0],ms[0][:-1]))

def chose(s,r,w):
	flg=True
	if r:
		r=r.replace('zh','zh-CN').replace('jp','ja')
		if w:
			w=w.replace('zh','zh-CN').replace('jp','ja')
		else:
			if r=='en':w='zh-CN'
			if r=='zh-CN':w='en'
	else:
		if w:
			if w=='en':r='zh-CN'
			if w=='zh-CN':r='en'
		else:
			r='zh-CN'
			w='en'
			j=trans(s,r=r,w=w)
			if j==None: 									r,w=w,r
			if isinstance(j[0][-1][-1],list):				r,w=w,r
			if ''.join(map(lambda x:x[0],j[0][:-1]))=='':	r,w=w,r
			if ''.join(map(lambda x:x[2][0][0],j[5]))==s:	r,w=w,r
	return r,w

def gtrans(s:str,r:str=None,w:str=None):
	if s.replace('\n','').replace('\t','').replace('\r','').replace(' ','')=='':
		return ''
	s=re.sub('^[\s]+','',s)
	r,w=chose(s,r,w)
	ms=js2ms(trans(s,r,w))
	return [ms,r,w]

print('import',__name__,'succ')
