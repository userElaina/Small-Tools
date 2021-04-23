def f(a,b=None,c:int=1):
	print('Func_f',a,b,c,ff)

def g(a,b,c='srbeb'):
	print('Func_g',repr(a),repr(b),repr(c),repr(gg))

hn=0
def h():
	global hn
	hn-=1
	print('Func_h',hn)

test_json={
	'tk':{
		'screen':(1430,920),
		'buttom':(200,100),
		'delta':(20,30),
		'w':(20,5),
		'/nick':'Q\u03c9Q',
	},
	'start':{
		'ff':{
			'/nick':'fffffff',
		},
		'gg':{
			'type':'eval',
			'v':2.71828,
		},
	},
	'func':[
		{
			'/name':h,
			'/mian':{
				'v':1,
			},
		},{
			'/name':h,
			'/nick':'hhhhh',
		},{
			'/name':h,
		},{
			'/name':f,
			'/mian':{
				'v':1,
				'/nick':'f1',
			},
			'-b':{
				'/nick':(1,'-b'),
				'type':str,
				'v':21421,
			},
			'-a':{
				'/nick':(2,'-a'),
				'type':eval,
				'v':[1,2,3],
			},
		},{
			'/name':'g',
			'/nick':'f1',
			'a':{
				'type':bool,
				'v':'X',
			},
			'b':{
				'type':'bool',
				'v':True,
			},
		},
	]
}

from tols.gui import testgui as qwq
a=qwq(js=test_json,ifname=True)
print('\n\n',a,'\n\n')
exec(a)
