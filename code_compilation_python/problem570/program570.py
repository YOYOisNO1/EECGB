def program570():
    r,g,b=list(map(int,input().split()))
    ans=min(r,g,b)+max(r-min(r,g,b))//3,0)+max(b-min(r,g,b))//3,0)+max(g-min(r,g,b))//3,0)
    print(ans)