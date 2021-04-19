from PIL import Image

def a2rgb_pil(rpth,wpth,depth,background):
	img=Image.open(rpth)
	img=img.convert('RGBA')
	sp=img.size
	width=sp[0]
	height=sp[1]
	for x in range(width):
		for y in range(height):
			dot=(x,y)
			color_d=list(img.getpixel(dot))
			if color_d[3]<depth:
				color_d=[background>>16,(background>>8)%0x100,background%0x100,255]
			else:
				color_d[3]=255
			img.putpixel(dot,tuple(color_d))
	img.save(wpth)
	

def a2rgb(rpth:str,wpth:str=None,depth:int=64,bg:int=0xffffff):
	if not wpth:
		wpth=rpth+'_'+'%06x'%bg+'.png'
	a2rgb_pil(rpth,wpth,depth,bg)
	return wpth


print('import',__name__,'succ')
