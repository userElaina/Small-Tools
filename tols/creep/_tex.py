import cairosvg
import matplotlib.pyplot as plt

from tols._u import *
from tols.creep._a2rgb import a2rgb

def md_plt(s,pth,img_size,text_size,axy,bxy):
	fig=plt.figure(figsize=img_size)
	f=fig.add_axes([0,0,1,1])
	f.get_xaxis().set_visible(False)
	f.get_yaxis().set_visible(False)
	f.set_xticks([])
	f.set_yticks([])
	plt.text(
		axy,
		bxy,
		s,
		fontsize=text_size,
		verticalalignment='center',
		horizontalalignment='center'
	)
	plt.savefig(pth)

def png_plt(s,pth,dpi,directly=True):
	if directly:s='$'+s+'$'
	md_plt(s,pth,(int(dpi/100),int(dpi/100)),int(dpi/10),0.5,0.5)


def png_cogs(s,pth,dpi):
	url=r'https://latex.codecogs.com/png.latex?\dpi{'+str(dpi)+'}'+urlencode(s)
	res=requests.get(url,headers=HEADERS)
	open(pth,'wb').write(res.content)

def svg_zhihu(s,pth):
	url=r'https://www.zhihu.com/equation?tex='+urlencode(s)
	res=requests.get(url,headers=HEADERS)
	open(pth,'wb').write(res.content)
	return res.text

def png_zhihu(s,pth,dpi):
	svg=svg_zhihu(s,pth+'.svg').replace(
		'text font-family=\"monospace\"',
		'text font-family=\"Sarasa Mono SC Nerd, Segoe UI Emoji\"'
	)
	cairosvg.svg2png(bytestring=svg,write_to=pth,dpi=dpi)


def tex(s:str,pth:str,api:str='zhihu',dpi:int=500,bg:int=None)->str:
	s=re.sub('[\s]+',' ',str(s)).replace('\\displaystyle','')
	while s[0]==' ':
		s=s[1:]
	while s[-1]==' ':
		s=s[:-1]
	
	if api=='plt':
		png_plt(s,pth,dpi)
		bg=None
	elif api=='zhihu':
		png_zhihu(s,pth,dpi)
	elif api=='cogs':
		png_cogs(s,pth,dpi)
	if isinstance(bg,int):
		pth=a2rgb(pth,bg=bg)
	return pth
	
if __name__=='__main__':
	s='Q\omega Q'
	tex(s,'zhihu.png')
	tex(s,'cogs.png',api='cogs')
	tex(s,'plt.png',api='plt')
	tex(s,'zhihu_b.png',bg=0x00ff00)
	tex(s,'cogs_b.png',api='cogs',bg=0xff0000)

print('import',__name__,'succ')
