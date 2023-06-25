def program3385():
    u,v=map(int, input().split())
    count=u/v
    if(count%2==1):
        print("YES")
    else:
        print("NO")