#coding=utf-8
class GetHeaders(object):
	def __init__(self):
		self.headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.33 Safari/537.36'},
						{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'},
						{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:49.0) Gecko/20100101 Firefox/49.0'},
						{'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'},
						{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"},
						{'User-Agent': "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1"},
						{'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3"},
						{'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"},
						{'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24"},
						{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
						]

	def get_headers(self):
		return self.headers
if __name__ == '__main__':
	a = GetHeaders().get_headers()
	print(a)
