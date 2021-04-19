'''
`inta2b` `intencode` `intdecode`

	>>> inta2b(s:str,a,b:int,sa,sb:str,same:str)->dict
	>>> same=['strict','replace','ignore']
'''

from tols._mian import *
from tols._basic import intencode,intdecode,re

b85ab=(
	'0123456789'
	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	'abcdefghijklmnopqrstuvwxyz'
	'!#$%&()*+-;<=>?@^_`{|}~'
)

mj=dict()
for i in range(len(b85ab)):
	mj[b85ab[i]]=i

def ints(a:all)->int:
	if not a:
		return None
	try:	
		return int(a)
	except:	
		a=str(a)
		if a in mj:	
			return mj[a]
		if a.startwith('byte'):
			return 0
		return None

def sab1(sa:str,same:str)->str:
	if not sa:
		return None
	sa=str(sa)
	if same=='replace':
		return sa
	s2=''.join(sorted(set(sa),key=sa.index))
	if len(sa)==len(s2):
		return sa
	if same=='ignore':
		return s2
	if same=='strict':
		return None
	return None	

def gs(s:str)->int:
	p='^\-?0[bB][01]+$'
	if re.match(p,s):
		return 2
	p='^\-?0[oO][0-7]+$'
	if re.match(p,s):
		return 8
	p='^\-?[0-9]+$'
	if re.match(p,s):
		return 10
	p='^\-?[0-9A-Fa-f]+$'
	if re.match(p,s):
		return 16
	p='^\-?0[xX][0-9A-Fa-f]+$'
	if re.match(p,s):
		return 16
	p='^\-?[0-9A-Za-z]+$'
	if re.match(p,s):
		return 36
	for i in s:
		if i not in b85ab:
			return 233
	return 85

def nx(a:int)->int:
	for i in [10,16,36,85]:
		if i>a:
			return i
	return 233

def sab2(a:int,sa:str)->str:
	a=abs(a)
	if not sa:
		sa=b85ab
	if len(sa)>=a:
		return sa[:a]
	for i in range(0x4e00,0xa000):
		sa+=chr(i)
		if len(sa)==a:
			return sa

def _inta2d(s:str,a:int,sa:str)->int:
	if 2<=a<=36 and b85ab.startswith(sa):
		return int(s,a)
	x=0
	if a==0:
		return intencode(s)
	d=dict()
	for i in range(len(sa)):
		d[sa[i]]=i
	b=False
	if s[0]=='-' and '-' not in sa:
		s=s[1:]
		b=True
	for i in s:
		x=x*a+d[i]
	if b:
		return -x
	return x

def _intd2b(d:int,b:int,sb:int)->str:
	s=''
	if b==0:
		return intdecode(d).decode(errors='backslashreplace')
	if b<0:
		while d:
			s=sb[d%b]+s
			d+=b+1
			d//=b
	else:
		if d<0:
			d=-d
		while d:
			s=sb[d%b]+s
			d//=b
	return s

def _inta2b(s:str,a:int,b:int,sa:str,sb:str)->dict:
	x={
		's':s,
		'a':a,
		'b':b,
		'sa':sa,
		'sb':sb,
	}
	if a in {-1,1} or b in {-1,1} or s=='':
		return x
	x['dec']=_inta2d(s,a,sa)
	x['hex']=hex(x['dec'])
	x['ans']=_intd2b(x['dec'],b,sb)
	if x['dec']<0 and b>0 and '-' not in sb:
		x['ans']='-'+x['ans']
	return x 

def inta2b(
	s:str,
	a:int=None,
	b:int=None,
	sa:str=None,
	sb:str=None,
	same:str='strict',
)->dict:

	if isinstance(s,int):
		a=10
		sa=b85ab[:10]
	
	s=str(s)	

	a=ints(a)
	b=ints(b)
	sa=sab1(sa,same)
	sb=sab1(sb,same)

	#!:sa<a,
	#?:sa<s,a or b in 0,1,-1
	#@:s-a-sa,a-b-sb
	#@a:a-sa,a-b-sb
	#@b:b-sb,(s+b)-a-sa
	#@sa:sa-a-b-sb
	#@sb:sb-b,(s+b)-a-sa
	#@x+x:x-sx
	
	if sa and a==None:
		a=len(sa)
	if sb and b==None:
		b=len(sb)

	if a==None:
		a=gs(s)
		if a==b:
			a=nx(a)
	
	if b==None:
		b=16 if a==10 else 10
	
	if abs(a)>500:
		a=0
	if abs(b)>500:
		b=0
	if len(s)>500:
		s=''

	sa=sab2(a,sa)
	sb=sab2(b,sb)
	
	if 2<=abs(a)<=36 and b85ab.startswith(sa.upper()):
		s=s.upper()
		sa=sa.upper()

	if a not in {0,1,-1}:
		s=''.join([i for i in s if i in sa])

	return _inta2b(s,a,b,sa,sb)

def test():
	s=input()
	while s!='w':
		s=input()
		if s.startswith('exit'):
			exit()
	s=input('w!\n')
	x=re.findall('[\S]+[\s]*=[\s]*[\S]+',s)
	print(x)
	a=[re.sub('[\s]+','',i).split('=') for i in x]
	print(a)
	x={
		's':None,
		'a':None,
		'b':None,
		'sa':None,
		'sb':None,
		'same':'cp',
	}
	for i in a:
		x[i[0]]=i[1]
	if not x['s']:
		x['s']=input('ur ws?\n')
	print(x)
	ans=inta2b(x['s'],x['a'],x['b'],x['sa'],x['sb'],x['same'])
	for i in ans:
		print(i,ans[i])
	print('\n')


'''
asdfa
ww

w
a =K b= -2 sb=zo safd=b
12
oozozoz

w
a=-2 b=85 sa=zo safd=b 
oozozoz
M

w
a=-2 b=85 sa=zo sb=!@ s=oozozoz
且

w
a=233 b=233 sa=abc sb=CBA s=cba
ABC

w
a=0 b=58 sb=123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz
ABDCDEFGA

w
sb=ABCDEFGHIJKLMNOPQRSTUVWXYZ234567 b=32 a=0
qwqwq

exit
'''


print('import',__name__,'succ')
