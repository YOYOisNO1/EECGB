def program5449():
    r,g,b=map(int,input().split())
    bou=0
    l=min(2,r,g,b)
    for m in range(l+1):
        x=m+sum((i-m)//3 for i in [r,g,b])
        if x>bou:
            bou=x
    print(bou)