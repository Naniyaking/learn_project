# coding = utf-8
import  requests
import re

import urllib
import  urllib3
import shutil


from bs4 import BeautifulSoup
import os

class get_img():
    def test_ur(self, url):
        start_html = self.req_url(url)
        soup = BeautifulSoup(start_html.text, 'html.parser')
        for link in soup.find_all('img',):
            print(link['src'])


    def all_url(self, url):
        start_html = self.req_url(url)
        soup = BeautifulSoup(start_html.text, 'html.parser')
        # print(soup.find_all('a'))

        for link in soup.find_all('img',):

            # print(link['href'])
            uri = link['src']
            img_url = "http:" + uri
            large_url = img_url.replace("mw600", "large")

            name = large_url[-9:-4]
            img = self.req_url(large_url)
            with  open(name + '.jpg', 'ab') as f:
                   f = open(name + '.jpg', 'ab')
                   f.write(img.content)
                   f.close()



    def req_url(self, url):
        header = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Cookie': '_ga=GA1.2.1356614339.1565864648; _gid=GA1.2.140068191.1565864648'

        }

        content = requests.get(url, headers=header, )
        return content
    def  compare_pic(self, dir_1, dir_2,):
         dir_one = dir_1
         dir_two = dir_2
         pic_name_one = os.listdir(dir_one)
         pic_name_two = os.listdir(dir_two)
         same_pic = [x for x in pic_name_one if x in pic_name_two ]
         print(same_pic)
         os.chdir(dir_two)
         for pic_name in same_pic:
             os.remove(pic_name)







if __name__ == '__main__':
    # pic_dir = ""
    # get_img = get_img()
    # jian_pic_url = "http://jandan.net/"
    # jian_pic_url = "http://jandan.net/"
    # os.chdir(pic_dir)
    # for i in range(1, 16):
    #     url = jian_pic_url+"page-"+str(i)+"#comments"
    #     print(url)
    #     get_img.all_url(url)
    # url = "https://www.qiushibaike.com/"

    # get_img.test_ur(url)
    set_dir_1 = ""
    set_dir_2 = ""

    get_img = get_img()
    get_img.compare_pic(set_dir_1, set_dir_2)





