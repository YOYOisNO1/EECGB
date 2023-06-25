def program2813():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Aug 27 02:21:06 2020
    
    @author: Dark Soul
    """
    [n,k]=list(map(int, input().split()))
    cnt0=0
    n=str(n)
    for i in range(len(n)):
        if n[i]=='0':
            cnt0+=1
    if cnt0>=k:
        sol=0
        rem0=0
        for i in range(len(n)-1,-1,-1):
            if n[i]!='0':
                sol+=1
            else:
                rem0+=1
            if rem0==k:
                break
        print(sol)
    else:
        if cnt0==0:
            print(len(n))
        else:
            print(len(n)-1)
                