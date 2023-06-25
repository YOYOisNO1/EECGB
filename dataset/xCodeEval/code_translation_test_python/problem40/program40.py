def program40():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    c = 0
    
    while a:
        if a[0] > k and a[-1] > k:
            break
    
        if a[0] <= k:
            a.pop(0)
            c += 1
        elif a[-1] <= k:
            a.pop()
            c += 1
    
    print(c)