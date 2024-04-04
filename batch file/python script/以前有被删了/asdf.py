import requests
import parsel
from fake_useragent import UserAgent
ua = UserAgent()
base = 'https://www.soushushu.com/plugin.php?id=mz_reader:mzreader&tid=335249&aid=1114188&page='
count = 0
while count < 90:
	count +=1
	url = base + str(count)
	user_agent = ua.chrome#firefox最容易出问题？反正用这个90次没出问题
	headers = {'user-agent': user_agent}
	result = requests.get(url, headers=headers)
	if result.status_code != 200:
		count-=1
	else:
		selector = parsel.Selector(result.text)
		paragrah = selector.css('#txt_content p ::text').getall()
		bbbb= '\n'.join(paragrah)
		with open('逆天邪神番外51.txt', mode='a', encoding = 'utf-8') as f:
			f.write('\n')
			f.write(bbbb)
			f.write('\n')
	print(count)

#print(result.text)





#alsdf = selector.css('p.txt_content::text').getall()
#alsdf = selector.xpath('//p[has-class("content_detail")]').getall()

#print(paragrah)
#print(alsdf)
#print(bbbb)