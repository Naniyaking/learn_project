# coding:utf-8


import os

def  pip_install_by_tsinghua(module_name):

    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  "+module_name)


def pip_istall_target_dir(target_dir, module_name):
    get_target_dir ="--target="+target_dir
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  "+get_target_dir+" "+module_name)

    print("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  "+get_target_dir+" "+module_name)

    
if __name__ == '__main__':
    print("please input  module name: ")
    set_moudle_name =input()
    print("please input  dir: ")

    set_dir = input()
    if set_dir == "" or set_dir ==None  :

        pip_install_by_tsinghua(set_moudle_name)
    else:
        pip_istall_target_dir(set_dir,  set_moudle_name)

    


   
