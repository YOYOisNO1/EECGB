def program4486():
    n = int(input())
    m = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    
    k = 0
    q = 0
    
    for i in range(n):
        k += a[i]
        if a[i] > q:
            q = a[i]
    
    
    k += m
    
    if k % n != 0:
        if q <= k // n + 1:
            print(k // n + 1, m + q)
        else:
            print(q, m + q)
    else:
        if q <= k // n:
            print(k // n, m + q)
        else:
            print(q, m + q)