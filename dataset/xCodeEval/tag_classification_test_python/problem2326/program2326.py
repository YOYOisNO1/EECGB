def program2326():
    a,b = map(int,input().split())
    c = min(a,b)
    d = a-c
    e = b-c
    f = max(a,b)
    g = (f-c)//2
    print(c, g)
    
    