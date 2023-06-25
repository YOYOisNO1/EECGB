def program880():
    s=0
    a,b,c=map(int,input().split())
    s+=2*c
    x=min(a,b)
    a-=x
    b-=x
    s+=2*x
    if a>0:
        s+=1
    if b>0:
        s+=1
    print(s)