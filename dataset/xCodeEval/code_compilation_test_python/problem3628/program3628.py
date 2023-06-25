def program3628():
    n, l,r = map(int, input().split())
    
    a = [0]
    if r == l:
        print 0
        exit()
    
    while n >= 2:
        a.append(n % 2)
        n /= 2
    ans = r - l + 1  
    for i in range(1, len(a)):
        if a[i] == 0:
            d = len(a) - i + 1
            ans -= len([j for j in range(l, r + 1) if j % (2**(d)) == 2**(d-1)])
            
    print ans