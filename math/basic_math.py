# coding:utf-8

def get_num(num):
    if num == 1:
       print(num,"不是素数")
    else:
    
        for i in range(2,num):
            if  num % i == 0:#取余等于0,说明能被整除
                # print(i)
                print(num,"不是素数")
                j = int(num/i)   
                print(j,"*",i,"=",num)
                break 
        else:
            # print(num)
            print(num,"是素数")

    
        
        

        
    # print(num,"是素数")

if __name__ == '__main__':
    for num in range(1, 100):
        get_num(num)
    # print(95 % 2)
