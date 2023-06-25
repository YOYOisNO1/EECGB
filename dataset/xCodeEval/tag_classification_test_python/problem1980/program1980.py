def program1980():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Jan 26 22:18:23 2017
    
    @author: USER PC
    """
    
    n,m,k=input().split(" ")
    n,m,k=int(n),int(m),int(k)
    ans=1
    m-=n
    a=0
    b=0
    c=a+b+1
    while m>=c:
        ans+=1
        m-=c
        if(a<k-1): a+=1
        if(b<n-k): b+=1
        if(a==k-1 and b==n-k): break
        c=a+b+1
    ans+=m//n
    print(ans)