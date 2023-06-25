def program6046():
    l,d,v,g,r=map(float,input().split())
    t1=d/v
    answ=t1+(l-d)/v
    while(t1>g+r):t1-=(g+r)
    if(t1>=g):answ+=((g+r)-t1)
    print(answ)