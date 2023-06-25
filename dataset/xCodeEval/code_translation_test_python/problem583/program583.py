def program583():
    n,m = [int(i) for i in input().split()]
    k = 0
    while n>=2 and m>=1 or n>=1 and m>=2:
        if m>n: m,n,k = m-2,n-1,k+1
        else: m,n,k = m-1,n-2,k+1
    print(k)