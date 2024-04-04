with open(r'title.txt', encoding='utf-8') as f:
	tete=f.readlines()
	f.close()
with open(r'url.txt', encoding='utf-8') as fu:
	ust=fu.readlines()
	fu.close()
i=0
while i<203:
	print(tete[i])
	print(ust[i])
	i+=1