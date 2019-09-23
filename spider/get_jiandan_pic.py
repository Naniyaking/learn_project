# coding : utf-8

import os
import sys
import requests
from bs4 import BeautifulSoup
import datetime

home_path = ""

def get_date_str():
    n_year = str(datetime.datetime.now().year)
    n_month = str(datetime.datetime.now().month)
    n_day = str(datetime.datetime.now().day)
    n_date = ("%s%s%s"  % ( n_year, n_month, n_day))

    return n_date


def req_url(url):  ##这个函数获取网页的response 然后返回
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        # 'referer':  # 伪造一个访问来源 "http://www.mzitu.com/100260/2"
    }
    content = requests.get(url, headers=headers)
    return content


def create_dir(dir_name):
    isexist = os.path.exists(dir_name)
    if not isexist:
        os.mkdir(dir_name)
    else:
        print(dir_name+"is already exist!!!")

def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_pic_list (set_url):
    url_list =[]
    com_html = req_url(set_url)
    soup = BeautifulSoup(com_html.text, 'html.parser')
    for link in soup.find_all("a", attrs={"class":"view_img_link"}):
        uri =str(link['href'])
        pic_url = "http:"+uri
        url_list.append(pic_url)
    return url_list




if __name__ == '__main__':
    ooxx_url = "http://jandan.net/ooxx"
    ooxx_html = req_url(ooxx_url)
    ooxx_soup = get_soup(ooxx_html.text)
    # get_soup = BeautifulSoup(ooxx_html.text, 'html.parser')
    page_num = str((ooxx_soup.find(attrs={"class": "current-comment-page"})).text)[1:3]
    print(page_num)
    now_date = get_date_str()
    print(now_date)
    dir_name = home_path+now_date
    print(dir_name)
    create_dir(dir_name)
    for i in range(int(page_num)+1):

        page_url = "http://i.jandan.net/ooxx/page-"+str(i)+"#comments"
        # print(page_url)
        for get_pic_url in get_pic_list(page_url):
            # print(get_pic_url)
            get_pic_name = get_pic_url.split("/")[-1]
            # print(get_pic_name)
            pic_save_name = dir_name+"\\"+get_pic_name
            pic = req_url(get_pic_url)
            with open(pic_save_name, 'ab') as f:
                f.write(pic.content)
                f.close()



