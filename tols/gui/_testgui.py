# from json import loads,dumps
# from copy import deepcopy as dcp
from tols._mian import *
import tkinter as tk

_nick='/nick'
_mian='/mian'
_name='/name'
_type='type'
_v='v'

_js=None

def ck(d:dict,name:str):
	if _nick in d:
		d[_nick]=str(d[_nick])
	else:
		d[_nick]=name
	if _v not in d:
		d[_v]=''
	if _type not in d:
		d[_type]=type(d[_v])
	d[_v]=str(d[_v])

	if d[_type] in {bool,'bool'}:
		d[_type]='bool'
		if d[_v] in {'','0','None','False','false','f','F','x','X'}:
			d[_v]='False'
		else:
			d[_v]='True'
	elif d[_type] in {str,'str'}:
		d[_type]='str'
	else:
		d[_type]='eval'

def jsonchecker():
	global _js
	for i in _js['start']:
		ck(_js['start'][i],i)

	for i in _js['func']:
		for j in i:
			if j.startswith('/'):
				continue
			ck(i[j],j)
		if not isinstance(i[_name],str):
			i[_name]=i[_name].__name__
		if _nick in i:
			i[_nick]=str(i[_nick])
		else:
			i[_nick]=i[_name]

		if _mian not in i:
			i[_mian]={
				_nick:i[_nick],
				'type':'bool',
				'v':'False',
			}
		else:
			i[_mian][_nick]=i[_nick]
			i[_mian]['type']='bool'
		ck(i[_mian],_mian)


def upansj(i:str,j:dict,is1st:bool)->str:
	a='' if i.startswith('-') else (i+'=')
	if j['type']=='str':
		a+=repr(j['v']) if is1st else repr(j['v'][:-1])
	elif j['type']=='eval':
		a+=j['v'] if is1st else j['v'][:-1]
	else:
		a+=j['v']
	return a

def upans(js:dict,is1st:bool=False)->list:
	qwq=list()
	for i in js['start']:
		qwq.append(upansj(i,js['start'][i],is1st))
	for i in js['func']:
		if i['/mian']['v']=='False':
			continue
		b=i['/name']+'('
		for it in i:
			if it.startswith('/'):
				continue
			b+=upansj(it,i[it],is1st)+','
		b+=')'
		qwq.append(b)
	return qwq


bts=None
args=None
t=None
a3=None
ans=None
exec_allow=None


def f_press(i:int):
	i=int(i)
	if bts[i]['text']=='True':
		bts[i]['text']='False'
		bts[i]['bg']='white'
	else:
		bts[i]['text']='True'
		bts[i]['bg']='red'

MXN=10000
for i in range(MXN):
	od='def ff_'+str(i)+'():f_press('+str(i)+')'
	exec(od)


def f_run():
	global exec_allow
	# print('Run')
	f_up()
	exec_allow=True
	t.destroy()

def f_up():
	global ans
	# print('Update')
	rn=0
	for i in args:
		for j in i:
			if j['type']=='bool':
				j['v']=bts[rn]['text']
			else:
				j['v']=bts[rn].get('1.0',tk.END)
			rn+=1

	ans=upans(_js)
	a3.delete('0.0',tk.END)
	a3.insert(tk.END,'\n'.join(ans))
	# print(ans)

def testgui(
	js:dict=None,
	pth:str=None,
	ifname:bool=False,
	ico:str='./tols/gui/1.ico',
)->list:
	
	global bts,args,_js,t,a3,ans,exec_allow

	exec_allow=False

	if js:
		if isinstance(js,dict):
			_js=dcp(js)
		else:
			try:
				_js=json.loads(js)
			except:
				raise TypeError('urs json smjb.')
	elif pth:
		print('read')
		_js=openjs(pth)
	else:
		raise TypeError('ur args?')
	
	jsonchecker()
	ans=upans(_js,is1st=True)


	if pth:
		sve(pth,_js)

	dpix,dpiy=_js['tk']['screen']
	px,py=_js['tk']['buttom']
	dx,dy=_js['tk']['delta']
	s_wd,s_dw=_js['tk']['w']


	args=[[_js['start'][i] for i in _js['start']],]

	for i in _js['func']:
		arg=[i['/mian'],]
		for j in i:
			if j.startswith('/'):
				continue
			arg.append(i[j])
		args.append(arg)

	del t
	t=tk.Tk()
	t.geometry(str(dpix)+'x'+str(dpiy)+'+0+0')
	t.title(_js['tk']['/nick'])
	try:
		t.iconbitmap(ico)
	except:
		print('(without ico)')

	dpix-=dx+px+dx
	dpiy-=s_dw

	bts=list()

	falines=list()
	fas=list()
	tags=list()

	b=0
	for i in args:
		a=len(i)
		if a>b:b=a

	a=(px+dx)*b-dx+s_wd-s_dw
	b=(py+dy)*len(args)-dy+s_wd-s_dw

	tt=tk.Canvas(
		t,
		width=dpix,
		height=dpiy,
		scrollregion=(0,0,a,b),
		bg='#00ff00',
	)
	tt.place(x=0,y=0)

	ttf=tk.Frame(
		tt,
		width=a,
		height=b,
		bg='#00ffff'
	)
	ttf.place(x=0,y=0)

	svb=tk.Scrollbar(tt,orient=tk.VERTICAL)
	svb.place(x=dpix-s_wd+s_dw,y=0,width=s_wd,height=dpiy)
	svb.configure(command=tt.yview)
	shb=tk.Scrollbar(tt,orient=tk.HORIZONTAL)
	shb.place(x=0,y=dpiy-s_wd+s_dw,width=dpix,height=s_wd)
	shb.configure(command=tt.xview)

	tt.config(xscrollcommand=shb.set,yscrollcommand=svb.set)
	tt.create_window((a//2,b//2),window=ttf) 
	iy=0
	for i in args:
		yy=iy*(py+dy)
		jx=0
		faline=tk.Frame(
			ttf,
			width=(px+dx)*len(i)-dx,
			height=py,
			bg='#0000ff'
		)
		falines.append(faline)
		faline.propagate(False)
		faline.place(x=0,y=yy)
		for j in i:
			xx=jx*(px+dx)
			
			fa=tk.Frame(
				faline,
				width=px,
				height=py,
				bg='#ff00ff',
			)
			fas.append(fa)
			fa.propagate(False)
			fa.place(x=xx,y=0)

			tag=tk.Label(
				fa,
				text=j['/nick']+'.'+j['type'],
				font=('黑体',10,),
				wraplength=px,
			)
			tags.append(tag)
			tag.pack()

			if j['type']=='bool':
				a=tk.Button(
					fa,
					command=eval('ff_'+str(len(bts))),
					bg='#ff0000' if j['v']=='True' else '#ffffff',
					text=j['v'],
					font=('黑体',20,),
					bd=1,
				)
				a.pack(expand=True,fill=tk.BOTH)
			else:
				a=tk.Text(
					fa,
					bg='#ffffff',
					bd=1,
					font=('黑体',12,),
				)
				a.insert(tk.INSERT,j['v'])
				a.pack(expand=True,fill=tk.BOTH)


			bts.append(a)
			jx+=1
		iy+=1


	fa1=tk.Frame(
		t,
		width=px,
		height=py,
	)
	fa1.propagate(False)
	fa1.place(x=dpix+s_dw+dx,y=dy)
	a1=tk.Button(
		fa1,
		command=f_run,
		bg='#ffff00',
		text='Run',
		font=('黑体',20,),
		bd=0,
	)
	a1.pack(expand=True,fill=tk.BOTH)

	fa2=tk.Frame(
		t,
		width=px,
		height=py,
	)
	fa2.propagate(False)
	fa2.place(x=dpix+s_dw+dx,y=dy*2+py)
	a2=tk.Button(
		fa2,
		command=f_up,
		bg='#ffff00',
		text='Update',
		font=('黑体',20,),
		bd=0,
	)
	a2.pack(expand=True,fill=tk.BOTH)

	fa3=tk.Frame(
		t,
		width=px,
		height=dpiy-dy*4-py*2,
	)
	fa3.propagate(False)
	fa3.place(x=dpix+s_dw+dx,y=dy*3+py*2)
	a3=tk.Text(
		fa3,
		bg='#ffffff',
		bd=1,
		font=('黑体',12,),
	)
	a3.insert(tk.INSERT,'\n'.join(ans))
	a3.pack(expand=True,fill=tk.BOTH)

	s1=tk.Scrollbar(t)
	s2=tk.Scrollbar(orient=tk.HORIZONTAL)

	t.mainloop()

	if not exec_allow:
		ans='print(\'U closed the window!\')'
		raise RuntimeError('U closed the window!')

	if ifname:
		return '\n\t'.join(['if __name__==\'__main__\':',]+ans)
		
	return '\n'.join(ans)
