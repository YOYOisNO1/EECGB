def program3027():
    # -*- coding: utf-8 -*-
    """
    Created on Sat Mar 30 14:07:06 2019
    
    @author: avina
    """
    
    N = int(input())
    
    l = []
    
    while N:
        n = N;m = 0; p=1;
        while n :
            if n%10:
                m +=p
            n//=10
            p *= 10
       # print(m)       
        l.append(m)
        N -= m
    l.sort()
    print(len(l))
    print(*l)