def program224():
    # -*- coding: utf-8 -*-
    """
    Created on Fri Apr 27 00:39:17 2018
    
    @author: shubham
    """
    s = list(map(int, input().split()))
    count = 0
    for i in range(len(s)):
        x = 2*s
        c1 = 0
        if s[i]>0:
            m = s[i]
            x[i]=0
            x[i+14] = 0
            t = 0
            if m>14:
                t = m//14
                m%=14
            for j in range(i+1, i+15):
                x[j]+=t
            for j in range(i+1, i+m+1):
                x[j]+=1
            for j in range(len(x)):
                if x[j]%2==0:
                    c1+=x[j]
            if c1>count:
                count = c1
            
    print(count)
                