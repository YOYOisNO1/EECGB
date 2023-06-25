def program109():
    l, r = map(int, input().split())
    if r-l < 2 or r==3:
        print -1
    elif r%2==0:
        print r-2,r-1,r
    else:
        print r-3,r-2,r-1