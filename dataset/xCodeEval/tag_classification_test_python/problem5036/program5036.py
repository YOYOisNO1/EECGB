def program5036():
    w,b,k,p,q=map(float,input().split()+[0,0,1])
    s=w+b
    while q and k<s:
        d=q*w/s
        p+=d;q-=d;s-=1
        d=q*w/s
        q-=d;s-=1;k+=1
    print(p)
    