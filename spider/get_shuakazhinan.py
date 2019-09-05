# coding: utf-8
import os
import re
from bs4 import BeautifulSoup
import requests
import re
import datetime


def  get_content(url):
    headers = {
        # 'Accept:' 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        "Accept-Encoding": "gzip, deflate, br",
        'Connection': 'keep-alive',
        # "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        # 'Cookie': 'q_c1=304c89e04241417dbb08d214c4d8faa1|1507539040000|1502690338000; d_c0="ABBCmkxCOgyPTmZUlf1gI-dmjnfM2IHk4ds=|1502848124"; __utma=51854390.1554283039.1502848126.1543378595.1548296610.12; __utmv=51854390.000--|2=registration_date=20160704=1^3=entry_date=20170814=1; q_c1=630cafd60487425d98e39fb28481a961|1548296608000|1508490065000; __DAYU_PP=zBF6jy7FeZYUMy3RREVn37f6bee236f7; _xsrf=uziwlDZl3VupoNrWxpsp8KdhJ03dHvqS; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; _zap=95a063cd-3661-47f7-bf2a-75581ec4120e'


    }
    set_url = url
    zhihu_html = requests.get(set_url, headers=headers, )
    return  zhihu_html.content

if __name__ == '__main__':
    t_year = str(datetime.datetime.now().year)
    t_month = str(datetime.datetime.now().month)
    t_day = str(datetime.datetime.now().day)
    now_date = ("%s%s%s%s%s" %  (t_year, "-", t_month, "-", t_day))
    print(now_date)

    url = "https://www.zrfan.com/category/zhinan/"
    soup = BeautifulSoup(get_content(url), 'html.parser')
    #print(soup.prettify())
    num = 1
    for link in soup.find_all('h2'):
          get_text = str(link.get_text())
          result = now_date in get_text
          if result == True:
              print(type(link))
              print(link.a['href'])
              new_url = "http:"+ link.a['href']
              print(new_url)
              new_soup = BeautifulSoup(get_content(new_url), 'html.parser')
              for new_link in new_soup.find_all("blockquote"):
                  print(str(num)+"、"+new_link.get_text())
                  num=num+1

        # text_content = str(link.get_text())
        # print(text_content)
        # result = today in text_content
        # if result == True:
        #       print(link)

        # bank_name = bank_text[0:4]
        # if bank_name == "浦发银行":
        #     print(bank_text)



