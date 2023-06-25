def program3853():
    r,h = map(int, input().split())
    
    ans = 0
    
    ans += 2*(h/r)
    x=h%r
    
    if 4*x>=3*r*r:
        ans += 3
    elif 2*x>=r:
        ans += 2
    else:
        ans += 1
    
    print ans