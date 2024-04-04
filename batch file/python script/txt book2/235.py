import requests
from bs4 import BeautifulSoup
import parsel
# 要爬取的网页的URL
url = 'https://www.kanunu8.com/book2/11104/'  # 请将URL替换为你要爬取的网页URL

# 发送GET请求并获取网页内容
with open('counter.txt', "r+") as fi:
    data = fi.read()
i = int(data)
while i<208637:
	response = requests.get(url+str(i)+'.html')
	response.encoding=response.apparent_encoding
	# 检查响应状态码
	if response.status_code == 200:
		# 解析网页内容
		soup = BeautifulSoup(response.text, 'html.parser')

		#查找文章标题
		tile= soup.find('h1')
		for t in tile:
			print(t.text)
			print(i)
			with open('和我有缘.txt',mode='a',encoding='utf-8') as f:
				f.write(t.text)
				f.write('\n')
		
		# 查找文章正文
		p_tags = soup.find_all('p')
		p_tags.pop()
		p_tags.pop()
		# 打印所有<p>标签的文本内容
		asdf=0
		for p in p_tags:
			if(asdf!=0):
				with open('和我有缘.txt',mode='a',encoding='utf-8') as f:
					f.write(p.text)
			asdf=asdf+1

	else:
		print('无法访问网页，状态码:', response.status_code)
	i=i+1
