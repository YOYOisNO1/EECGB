def program1127():
    # -*- coding: utf-8 -*-
    """
    Created on Fri May 22 13:59:32 2020
    
    @author: dell
    """
    
    n=int(input())
    l=[x for x in map(int,input().split())]
    li=l[:]
    k=0
    pages=0
    while pages<n:
        pages+=li[k%7]
        k+=1
        k=k%7
    print(7 if k==0 else k)