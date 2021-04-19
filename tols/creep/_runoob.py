from tols._u import *

_runoob_set0={
    'r':'R',
    'vb':'vb',
    'ts':'ts',
    'typescript':'ts',
    'kt':'kt',
    'kotlin':'kt',
    'pas':'pas',
    'pascal':'pas',
    'lua':'lua',
    'node.js':'node.js',
    'nodejs':'node.js',
    'js':'node.js',
    'go':'go',
    'golang':'go',
    'swift':'swift',
    'rs':'rs',
    'rust':'rs',
    'sh':'sh',
    'bash':'sh',
    'pl':'pl',
    'perl':'pl',
    'erl':'erl',
    'erlang':'erl',
    'scala':'scala',
    'cs':'cs',
    'c#':'cs',
    'csharp':'cs',
    'cpppp':'cs',
    'c++++':'cs',
    'c艹艹':'cs',
    'rb':'rb',
    'ruby':'rb',
    'cpp':'cpp',
    'c++':'cpp',
    'c艹':'cpp',
    'c':'c',
    'java':'java',
    'py3':'py3',
    'py':'py3',
    'py2':'py',
    'php':'php',
}
_runoob_set1={
    'R':80,
    'vb':84,
    'ts':1001,
    'kt':19,
    'pas':18,
    'lua':17,
    'node.js':4,
    'go':6,
    'swift':16,
    'rs':9,
    'sh':11,
    'pl':14,
    'erl':12,
    'scala':5,
    'cs':10,
    'rb':1,
    'cpp':7,
    'c':7,
    'java':8,
    'py3':15,
    'py':0,
    'php':3
}

url='https://tool.runoob.com/compile2.php'

def runoob(
	s:str='print(\'Hello world!\')',
	pl:str='py3',
	stdin:str=''
):
	pl=_runoob_set0[pl]
	payload={
		'code':s,
		'token':'4381fe197827ec87cbac9552f14ec62a',
		'stdin':stdin,
		'language':_runoob_set1[pl],
		'fileext':pl,
	}
	res=requests.post(url=url,headers=HEADERS,data=payload)
	return res.json()

def strunoob(
	s:str='print(\'Hello world!\')',
	pl:str='py3',
	stdin:str='',
):
	d=runoob(s,pl,stdin)
	return 'Output:\n'+d['output']+(
		('\nErrors:'+d['errors']) if d['errors']!='\n\n' else ''
	)

if __name__=='__main__':
	print(strunoob('print(1)\nprint(i)'))

print('import',__name__,'succ')
