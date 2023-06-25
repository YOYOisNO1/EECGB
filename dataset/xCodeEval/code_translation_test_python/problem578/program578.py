def program578():
    a=map(int,input().split())
    print(max(0,min(a[:4]+[a[-1]+1])-a[-2]))