#*-*coding=utf-8*-*
# time:2018-9-24

# 抓取下载网页的标题,图片和迅雷链接地址
# 由于该网站没有反爬措施,因此后面的时间延迟就pass掉

import requests
import codecs
import time
from lxml import etree

# 宅男福利首页抓取,获取每一个视频的链接
def fuli_index(n):
    #第一页
    # url = 'http://www.521dyw.com/leibie/index/id/17/p/1.html.html'
    f = codecs.open('zhainanfuli.txt', 'w', encoding='utf-8')
    # 简易下载,直接拖动到迅雷全部可以下载下来
    f2 = codecs.open('zhaina_jianyi.txt', 'w', encoding='utf-8')
    for n in range(1,n+1):
        #构造每页url:
        url = 'http://www.521dyw.com/leibie/index/id/17/p/' + str(n) + '.html' + str(n) + '.html'
        print url
        url_start = 'http://www.521dyw.com'
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        response = requests.get(url,headers=header )
        # print response.text
        html = etree.HTML(response.text)

        #取出每一个视频的链接地址:   一个列表15个地址左右
        url_shipin_list = html.xpath('//div[@class="boutlist"]/ul/li/a/@href')
        print url_shipin_list
        # 进入每一个具体视频网址,取出对应的标题和url
        # i = 1
        # f = codecs.open('zhainanfuli5.txt','a',encoding='utf-8')
        # # 简易下载,直接拖动到迅雷全部可以下载下来
        # f2 = codecs.open('zhaina_jianyi.txt', 'w', encoding='utf-8')
        f.write(u'----------------------第%d页内容------------------'%n + '\n')
        f2.write(u'----------------------第%d页内容------------------' % n + '\n')
        for shipin in url_shipin_list:
            url_shipin = url_start + shipin
        #     time.sleep(i)
            response2 = requests.get(url_shipin,headers=header)
            response2.encoding='utf-8'
            html2 = etree.HTML(response2.text)
            #取出详细视频页面的标题和迅雷下载地址:
            biaoti = html2.xpath('//div[@class="info"]/h1/text()')[0]
            url_xunlei = html2.xpath('//div[@class="down_list"]/ul/li/p/a/@href')
            # 鉴于,页面中有写迅雷下载地址丢失,故此判断
            if len(url_xunlei) >=1:
                print 'biaoti,url',biaoti,url_xunlei[0]
                # 写入文档
                f.write(u'标题:'+biaoti+' =====  '+u'迅雷下载地址:   '+ url_xunlei[0]+'\n')
                f2.write(url_xunlei[0]+'\n')
                # 模拟访问点击时间
                # if i <7:
                #     i+=1
                # elif i >7:
                #     i -= 1
                # elif i <1 :
                #     i = 2
    f.close()
    f2.close()


if __name__ == '__main__':
    fuli_index(22)


