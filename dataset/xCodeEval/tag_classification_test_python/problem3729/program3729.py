def program3729():
    from math import ceil
    
    n, t, k, d = map(int,input().split())
    
    T1 = ceil(n/k)*t #time of one oven
    C2 = ceil(d/t)*k #cakes while building new oven
    n_rem = n - C2   #cakes remaining while building 2nd
    
    if n_rem<0:
        n_rem = 0
    
    T2 = d + max(ceil(n_rem/(2*k))*t, ceil(C2/k)*t - d)
    
    if T1>T2:
        print("YES")
    else:
        print("NO")