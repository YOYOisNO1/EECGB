def program5357():
    (n, x, y) = map(int, input().strip().split())
    
    p = n*(y*0.01)
    if round(p) == p:
        m = int(p)-x
    else:
        m = int(p)+1-x
    
    if m >=0:
        print(m)
    else:
        print(0)