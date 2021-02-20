# coding: utf-8


import os
import time


def Create_dir_today(target_dir):
    if not os.path.exists(target_dir):
        
        os.makedirs(target_dir) //逐级创建目录
    else:
        print(target_dir+" already   exist!!")





if __name__ == "__main__":
    # print(time.time())
    # print(datetime.)
    basic_path = "D:\\work\\"


    get_year =  time.strftime("%Y") //获取当前年
    get_month =  time.strftime("%m") //获取当前月
    get_day =  time.strftime("%d")   //获取当前的天

    print(get_year)
    print(get_month)
    print(get_day)

    target_dir = basic_path+get_year+"\\"+get_month+"\\"+get_day //拼接目录
    Create_dir_today(target_dir)








