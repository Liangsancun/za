#coding=utf-8
from bs4 import BeautifulSoup as bs
import requests
import time

class GetProxies(object):
	def __init__(self,page_num=5):
		self.proxies = []
		self.page_num = page_num
		self.get_proxies_list()

	def get_proxies_list(self):
		print("正在获取代理列表...")
		head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'}

		for i in range(1,self.page_num+1):# 实际是1~slef.page_num
			print('\r 正在抓取%d:%d'%(i,self.page_num),end='')
			time.sleep(0.3)
			url="http://www.xicidaili.com/nn/"+str(i)
			# 抓取页面
			result = requests.get(url=url, headers=head).text

			soup = bs(result, 'lxml')
			# soup.find(标签，参数)只返回第一个结果，find_all返回所有的结果
			raw_ips = soup.find('table', id='ip_list').find_all('tr')

			# range(0,5)从0开始，默认步长为1，到4
			# 因为第一个没有ip地址，是表头
			for i in range(1, len(raw_ips)):
				ip_info = raw_ips[i]
				tds = ip_info.find_all('td')
				# 速度  class是被python内置，故用class_代替class
				string = tds[6].find('div', class_="bar")['title']
				string = string.replace('秒', '')
				# 存活时间
				live_time = tds[8].text

				# 速度小于1s 存活时间不是分钟，就保留
				num = int(float(string))
				if num <= 1 and '分钟' not in live_time:

					# 连接方式
					ip_style = tds[5].text.strip()
					if ip_style == 'HTTP':
						style = 'http'
					else:
						style = 'https'

					# 捕获一个代理 {'http':'124.24.23.54:8080'}
					proxy = {}
					proxy[style] = tds[1].text + ':' + tds[2].text
					# 添加到代理池
					self.proxies.append(proxy)


		print("代理列表抓取成功")




	def get_proxies(self):
		return self.proxies

if __name__ == '__main__':
	a = GetProxies(page_num=1).get_proxies()
	print(a)
