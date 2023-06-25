def program611():
    n,a,b = map(int,input().split())
    pos = n-a
    if pos <= b: print(pos)
    else:print(b+1)