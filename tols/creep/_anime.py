from tols._u import *

def anime(u:str)->list:
	u='https://trace.moe/api/search?url='+u
	res=requests.get(u,headers=HEADERS)
	d=res.json()
	# print(d)
	return [(i['anime'],int(i['at']),) for i in d['docs']]

def stranime(u:str)->str:
	ans=list()
	l=list()
	for i in anime(u):
		if i[0] in l:
			continue
		l.append(i[0])
		ans.append((i[0]+' ('+str(i[1]//60)+'\''+str(i[1]%60)+'\'\')'))
	return '\n'.join(['Total '+str(len(ans)),]+ans)


if __name__=='__main__':
	s='https://i.loli.net/2021/04/19/NfHrFoWCsp1DauT.png'
	print(stranime(s))

print('import',__name__,'succ')
