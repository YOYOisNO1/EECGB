def program777():
    [n,k]=[int(x) for x in input().split()]
    n+=1
    m=(k-(n%k))
    if m===k:
        m=0
    print m+n