import get_proxies
import get_headers
import random


if __name__ == '__main__':

	# 全局变量 格式[{'http':'http://www.baidu.com:8080'},]
    proxies = get_proxies.GetProxies(page_num=1).get_proxies()
	# 获取头部池 [{'User-Agent': "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"},]
    headers = get_headers.GetHeaders().get_headers()

	# 每次随机获取一个代理ip和头部
    proxy = random.choice(proxies)
    header = random.choice(headers)

    print(proxy,header)


