    # -*- coding: utf-8 -*-
    # @Author: HaonanWu
    # @Date:   2017-02-25 17:10:26
    # @Last Modified by:   HaonanWu
    # @Last Modified time: 2017-02-25 17:20:56
    
    n = input()
    home = input()
    dic = {}
    
def plus(dic, str):
        if dic.has_key(str):
            dic[str]+=1
        else:
            dic[str]=1
    
def minus(dic, str):
        if dic.has_key(str):
            dic[str]-=1
        else:
            dic[str]=-1
    
    for T in range(n):
        tmp = input().split('->')
        if tmp[0] == home:
            plus(dic, tmp[1])
        else:
            minus(dic, tmp[0])
    
    
    for item in dic.items():
        if item[1] != 0:
            print("contest")
            exit(0)
    
    print("home")
    