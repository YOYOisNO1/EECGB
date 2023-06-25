def program531():
    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
    """
    Created on Wed Sep 20 18:26:44 2017
    
    @author: soham
    """
    
    n,x=input().split()
    n=int(n)
    x=int(x)
    arr=map(int,input().split())
    arr.sort()
    count=0
    temparr=[0]*101
    for i in range(n):
        temparr[arr[i]]+=1
    for i in range(0,x):
        if temparr[i]==0:
            count+=1
    if temparr[x]>0:
        count+=temparr[x]
    
    print(count)
        
        
        