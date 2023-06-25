def program3981():
    [n, m, k] = input("").split(" ")
    [n, m, k] = [int(n), int(m), int(k)]
    
    a = [0 for i in range(0, n*m)]
    
    for i in range(0, n):
        for j in range(m):
            a[i+n*j] = (i+1)*(j+1)
    a.sort()
    print a[k-1]