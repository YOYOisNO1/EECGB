def program450():
    s=sum(map(int,input().split()))
    if s==0 or s%5!=0:print(-1)
    else:print(s//5)