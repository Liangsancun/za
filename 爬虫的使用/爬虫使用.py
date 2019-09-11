import my_db
import random
import requests
import json
import re
import time


class Spider(object):
    def __init__(self,xici_orderId,urls,outfile_pathes,one_save_num,db_info):
        self.headers = [{'User-Agent': 'Baiduspider+(+http://www.baidu.com/search/spider.html)'},
                        {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'},
                        {'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'},
                        {'User-Agent': 'Googlebot/2.1 (+http://www.google.com/bot.html)'},
                        {'User-Agent': 'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)'},
                        {'User-Agent': "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"},
                        {'User-Agent': "iaskspider/2.0(+http://iask.com/help/help_index.html)"},
                        {'User-Agent': "Mozilla/5.0 (compatible; iaskspider/1.0; MSIE 6.0)"},
                        {'User-Agent': "Sogou web spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"},
                        {'User-Agent': "Sogou Push Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"},
                        ]
        self.xici_orderId = xici_orderId
        self.table_num = len(self.outfile_pathes)
        self.arrs = []
        #有几张表，就在一个空数组中，装几个空数组 eg: 2个表 arrs=[[],[]]
        #arrs[0],arrs[1]分别装了表1和表2的数据，都是二维数组（其中一个一维数组是一个表中的一行）
        for i in range(self.table_num):
            self.arrs.append([])

        self.outfile_pathes = outfile_pathes
        self.urls = urls
        self.one_save_num = one_save_num
        # 连接数据库
        self.db = my_db.DB(db_info['host'], db_info['database'], db_info['user'], db_info['passed'], db_info['port'])

        #进行爬取
        self.spider_urls()


    def get_info(self,html,url):
        '''
        :param html:获取的源码
        :param url:
        :return:从源码中获取的信息
        '''
        one = [] #one中每一个元素都是二维数组，2个表时，初始one为[[],[]]  与arrs对应，one中一个数组就是从一个网页源码中获取的信息，并与arrs对应
        for i in range(self.table_num):
            one.append([])
        '''
        设置规则，并获取信息，将其添加到数组中
        
        
        '''

        print(one) #one中每一个元素都是二维数组
        return one

    def change_proxy_header(self):
        header = random.choice(self.headers)
        proxy ={}
        aa = requests.get(url='http://api3.xiguadaili.com/ip/?tid='+str(self.xici_orderId)+'&num=1&delay=1&protocol=https&filter=on')
        aa.close()
        proxy['https'] = aa.text

        return proxy,header

    def save_one_time(self):
        # 以存数据库的一条为一行（即一个一维数组为一行）
        for i in range(self.table_num):
            arr = self.arrs[i] #第i+1个二维数组(从1开始）是第i+1个表的数据
            outfile_path = self.outfile_pathes[i]#对应的该数组要存入的文件名
            table_name = outfile_path.split('.txt')[0] # 'hotels.txt'->'hotels'

            #每一个都是二维数组，一个是一个数据库中的条目

            '''
            # 插入数据库
            if len(arr)==1: #如果二维数组中只有一个元素，[[1,2,3]]，正常插入
                arr = arr[0] #
                # 存入数据库相应表中 #插入时，executemany(sql,[[1,2]])，正常插入
                self.db.insert_to_table(table_name, arr, 1)
            else:
                #len(arr[0])==1:#如果二维数组中的数组都是只有一个元素[[1],[2]]，跟正常的一样
            '''
            self.db.insert_to_table(table_name, arr, self.one_save_num)
            # 保存
            with open(outfile_path, 'a', encoding='utf-8') as f:
                for one in arr:
                    # 一个一维数组为一行
                    f.write(json.dumps(one, ensure_ascii=False) + '\n')




    def get_clear(self):
        for i in range(self.table_num):
            self.arrs[i].clear()
            #将self.arrs变为[[],[],]

    def spider_urls(self):

        # 每次随机获取一个代理ip和头部
        proxy, header = self.change_proxy_header()

        length = len(self.urls)
        for i in range(length):
            print('\r 下标%d:长度%d' %(i,length,), end='')
            time.sleep(0.3)
            if i%300 == 0:
                # 更换代理池和头部
                proxy, header = self.change_proxy_header()
            url = self.urls[i]
            req = ''
            # req有返回值（requests.get连接异常时无返回值），有返回值，也可能为不是正常的页面
            while(req == ''):
                try:
                    req = requests.get(url=url, headers=header, proxies = proxy,timeout=(3,3))
                # except requests.exceptions.Timeout or requests.exceptions.ProxyError or ConnectionRefusedError or ConnectionResetError or requests.exceptions.ConnectionError or socket.timeout or urllib3.exceptions.ReadTimeoutError as e:
                except Exception as e:
                    # print(repr(one args))可将'\n'打印出
                    print('超时，更换代理和头部', e, repr(url),repr(header),repr(proxy))
                    # 更换代理池和头部
                    proxy, header = self.change_proxy_header()
                    time.sleep(0.5)
                    # 无req.close()因为此时无返回req
            while(req.status_code != 200):  # 如果没有正常获得数据
                req.close()  # 关闭连接
                req = ''
                # req有返回值（requests.get连接异常时无返回值），有返回值，也可能为不是正常的页面
                while (req == ''):
                    try:

                        req = requests.get(url=url, headers=header, proxies = proxy,timeout=(3,3))
                    # except requests.exceptions.Timeout or requests.exceptions.ProxyError or ConnectionRefusedError or ConnectionResetError or ConnectionRefusedError or requests.exceptions.ConnectionError or socket.timeout or urllib3.exceptions.ReadTimeoutError as e:
                    except Exception as e:
                        # print(repr(one args))可将'\n'打印出
                        print('超时，更换代理和头部', e, repr(url), repr(header), repr(proxy))
                        # 更换代理池和头部
                        proxy, header = self.change_proxy_header()

                        time.sleep(0.5)
                        # 无req.close()因为此时无返回req
            req.close()
            #one # 2个表时，初始one为[[],[]]  与arrs对应，one中一个数组就是从一个网页源码中获取的信息，并与arrs对应
            one = self.get_info(req.text, url)
            # 将一个页面中整合的信息，添加到总的数组arrs中
            for i in range(self.table_num):
                temp = one[i]#每个都是二维数组
                self.arrs[i].extend(temp)


            if len(self.hotels) >= self.one_save_num or i == length - 1:

                # 存储超过self.one_save_num条时或是最后一个连接（不超过self.one_save_num条）存一次
                self.save_one_time()
                #清空
                self.get_clear()



        # 关闭数据库连接
        self.db.close()



if __name__ == '__main__':
        '''
        使用，需修改get_info()里的内容，即爬取规则
        '''
        #爬取，保存数据，并上传到数组库，
        # 西刺购买代理ip的订单号，链接urls，保存文件名（eg， ['hotels.txt','comments.txt'])one_save_time(多少条信息存一次）,连接数据库的信息{'host':'25.35.24.6','database':'xx','user':'aa','passwd':'bb','port':3306}
        Spider(xici_orderId,urls,outfile_pathes,100,db_info)









