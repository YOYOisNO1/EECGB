def program3617():
    n,m=map(int,input().split())
    a=[0]*m
    for i in range(1,m+1):a[i*i%m]+=(n-i)//m+1
    print(sum(zip(a,(a+a)[n::-1])))