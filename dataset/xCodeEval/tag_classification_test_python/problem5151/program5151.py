def program5151():
    n, l,r = map(int, input().split())
    if n == 0:
        print(0)
        exit()
    if n == 1:
        print(1)
        exit()
    
    a = [0]
    
    while n >= 2:
        a.append(n % 2)
        n /= 2
    ans = r - l + 1  
    for i in range(1, len(a)):
        if a[i] == 0:
            d = len(a) - i + 1
            ans -= len([j for j in range(l, r + 1) if j % (2**(d)) == 2**(d-1)])
            
    print(ans)