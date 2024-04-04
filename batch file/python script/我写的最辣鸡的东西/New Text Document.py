import parsel

with open(r'html_using python.txt', encoding = 'utf-8') as f:
	data = f.read()
	f.close()
selector = parsel.Selector(data)
filename = selector.css('h2::text').getall()

i=1

for p in selector.css('p'):
	if (i % 2)==0 and i >=4:
		bb=(int)(i/2-2)
		if bb== 39 or bb==65 or bb==115 or bb==122 or bb==166 or bb==187:
			bb=bb+1
			i=i+2			
		print(filename[bb])
	print(p.xpath('.//@href').get())
	i=i+1
