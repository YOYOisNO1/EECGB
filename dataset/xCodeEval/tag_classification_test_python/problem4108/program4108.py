def program4108():
    y,b,r = map(int,input().split())
    k = min(y+2,b+1,r)
    print(3*k-3)