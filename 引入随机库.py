# -*- coding = utf-8 -*-
# @Time : 2022/4/2 22:42
# @Author :蒋大帅
# @File : 引入随机库.py
# @Software:PyCharm

import random  #引入随机库
x=random.randint(1,10)   #randint()指的是随机整数,是包括1和10的，即【1,10】
print(x)


number=input('请告诉我你想出什么（剪刀：0，石头：1，布：2）:')
system=random.randint(0,2)
if int(number)==system:
    print(system)
    print('平局！')
elif int(number)!=system:
    if int(number)==0 and system==2:
        print(system)
        print('恭喜你！你赢了！')
    elif int(number)==1 and system==0:
        print(system)
        print('恭喜你！你赢了！')
    elif int(number)==2 and system==1:
        print(system)
        print('恭喜你！你赢了！')
    else:
        print(system)
        print('哈哈，你输了！')
