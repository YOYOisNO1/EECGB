def program1789():
    h,n=map(int,input().split(" "))
    res=0
    s=0
    while(h!=0):
        res+=1
        if s^(n>(1<<(h-1))):
            res+=1<<(h) - 1
        else:
            s^=1
        if n>1<<(h-1):
            n-=1<<(h-1)
    print(res)