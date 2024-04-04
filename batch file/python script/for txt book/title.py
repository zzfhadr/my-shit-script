import requests
import parsel
import time
from fake_useragent import UserAgent
ua = UserAgent()
url = 'https://m.xbequge.cc/wapbook/120/all.html?sort=1&page='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}
result = requests.get(url+'1', headers=headers)
#print(result.text)

selector = parsel.Selector(result.text)
filename = selector.css('span.title::text').get()
filename = filename.strip()


base = 'https://m.xbequge.cc'
with open('counter.txt', "r+") as fi:
    data = fi.read()
start = int(data)
counter = start
it=start/50+1
i = int(it)
if counter = 9999:
	i=99
s1=start%50
if s1 == 0:
	s1=50
while i < 79:
	page = url + str(i)
	result = requests.get(page, headers=headers)
	selector = parsel.Selector(result.text)
	paragrah = selector.css('#chapterlist p a::attr(href)').getall()
	#if here
	if i<78:
		for index, whatever in enumerate(paragrah):
			if index > s1 and index < 52:
				s1=1
				user_agent = ua.random
				headers = {'user-agent': user_agent}
				htmlsh = requests.get(base + whatever, headers=headers)
				selector2 = parsel.Selector(htmlsh.text)
				paragrah2 = selector2.css('#chaptercontent p ::text').get()
				texture = selector2.css('p.content_detail::text').getall()
				bbbb= '\n'.join(texture)
				texture = paragrah2.split('[')
				with open(filename + '.txt', mode='a', encoding = 'utf-8') as f:
					f.write(texture[0])
					f.write('\n')
					f.write(bbbb)
					f.write('\n')
				#second page
				x = whatever.split('.')
				htmlsh = requests.get(base + x[0] + '_2.html', headers=headers)
				selector2 = parsel.Selector(htmlsh.text)
				paragrah2 = selector2.css('#chaptercontent p ::text').get()
				texture = selector2.css('p.content_detail::text').getall()
				bbbb= '\n'.join(texture)
				texture = paragrah2.split('[')
				counter +=1
				with open('counter.txt','w') as fi:
					fi.write(str(counter))
				print(texture[0],counter)
				with open(filename + '.txt', mode='a', encoding = 'utf-8') as f:
					f.write('\n')
					f.write(bbbb)
					f.write('\n')
				time.sleep(1)
	else:
		for index, whatever in enumerate(paragrah):
			if index > s1 and index < 4:
				user_agent = ua.random
				headers = {'user-agent': user_agent}
				htmlsh = requests.get(base + whatever, headers=headers)
				selector2 = parsel.Selector(htmlsh.text)
				paragrah2 = selector2.css('#chaptercontent p ::text').get()
				texture = selector2.css('p.content_detail::text').getall()
				bbbb= '\n'.join(texture)
				texture = paragrah2.split('[')
				with open(filename + '.txt', mode='a', encoding = 'utf-8') as f:
					f.write(texture[0])
					f.write('\n')
					f.write(bbbb)
					f.write('\n')
				#second page
				x = whatever.split('.')
				htmlsh = requests.get(base + x[0] + '_2.html', headers=headers)
				selector2 = parsel.Selector(htmlsh.text)
				paragrah2 = selector2.css('#chaptercontent p ::text').get()
				texture = selector2.css('p.content_detail::text').getall()
				bbbb= '\n'.join(texture)
				texture = paragrah2.split('[')
				counter +=1
				print(texture[0],counter)
				if index == 3:
					counter = 9999
				with open('counter.txt','w') as fi:
					fi.write(str(counter))
				with open(filename + '.txt', mode='a', encoding = 'utf-8') as f:
					f.write('\n')
					f.write(bbbb)
					f.write('\n')
	i += 1
