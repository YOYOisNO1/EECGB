    ﻿"""
    Created on Tue Sep  4 00:25:14 2018
    
    @author: lenovo
    """
    
    #素数集合
    # 任何一个数字可以表示为2^(p1) * 3^(p2) * ... * k^(pn)
    # 其因子个数总数为 (p1 + 1) * (p2 + 1) * ... * (pn + 1)
    prime = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    # 到每个节点有传到该节点的值和因子总数、以及该取第几个元素
    min_value = round(1e18)
    n = int(input())
    
def search(value, total_factor, i):
        global min_value
        if total_factor == n:
            min_value = min(value, min_value)
            return 
        for k in range(1, 65):
            value *= prime[i]
            if value > min_value:
                break
            if total_factor * (k + 1) <= n:
                search(value, total_factor * (k + 1), i+1)
            
    search(1, 1, 1)    
    print(min_value)