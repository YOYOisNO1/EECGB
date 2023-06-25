def program7297():
    m,b = map(int,input().split())
    ans=0
    for y in range(b+1):
        x = (b-y)*m
        t = ((x+1)*(y+1)*(x+y))//2
        ans = max(ans,t)
    print(ans)