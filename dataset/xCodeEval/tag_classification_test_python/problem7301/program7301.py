def f(x):
        return x*(x+1)//2
    m, b = map(int, input().split())
    c,x,y,ans=0,0,0,0
    for y in range(b+1):
        x = (b-y)*m
        c = (x + 1) * f(y) + (y + 1) * f(x)
        ans=max(ans,c)
    print(int(ans))