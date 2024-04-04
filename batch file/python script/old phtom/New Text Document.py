import requests
import parsel
url = 'https://boxnovel.baidu.com/boxnovel/content?gid=4356298093&data=%7B%22fromaction%22%3A%22search_jingzhun%22%7D&cid=1569475103'


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'}
result = requests.get(url, headers=headers)
print(result.text)
#selector = parsel.Selector(result.text)



#paragrah = selector.css('#chaptercontent p ::text').get()
#alsdf = selector.css('p.content_detail::text').getall()
#alsdf = selector.xpath('//p[has-class("content_detail")]').getall()

#print(paragrah)
#print(alsdf)