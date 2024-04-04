import requests
import parsel
import time
from fake_useragent import UserAgent
ua = UserAgent()
url = 'https://quanben-xiaoshuo.com/n/yeyufuheilaogong-diaomanjiaoqi/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}

with open('counter.txt', "r+") as fi:
    data = fi.read()
i = int(data)
while i<1563:
	result = requests.get(url+str(i)+'.html', headers=headers)
	#print(result.text)
	selector = parsel.Selector(result.text)
	refilename= selector.xpath('//h1[has-class("title")]/text()').get()
	#print(refilename)
	filename = selector.xpath('//div[@id="articlebody"]//p/text()').getall()
	bbbb='\n'.join(filename)
	print(i)
	print(refilename)
	with open('和我有缘.txt',mode='a',encoding='utf-8') as f:
		f.write(refilename)
		f.write('\n')
		f.write(bbbb)
		f.write('\n')
	with open('counter.txt','w') as fi:
		fi.write(str(i))
	i=i+1