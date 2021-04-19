from MyQR import myqr

#28~ 6
#21~27 5
#14~20 4
#13~07 3
#06~01 2

def qrcode(s:str,pth:str,v:int=13,lv:str='H',pic:str=None):
	if pic:
		myqr.run(
			words=s, 
			version=v,
			level=lv,
			picture=pic,
			colorized=True,
			contrast=1.0,
			brightness=1.0,
			save_name=pth,
		)
	else:
		myqr.run(
			words=s,
			version=v,
			level=lv,
			colorized=False,
			contrast=1.0,
			brightness=1.0,
			save_name=pth,
		)
	return pth

if __name__=='__main__':
	qrcode('qwq','qwq2.png',)

print('import',__name__,'succ')
