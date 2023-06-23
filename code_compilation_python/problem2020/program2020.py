def program2020():
    n,k=map(int,input().split())
    for a on range(n+1):
        b=n-a
        if a*(a+1)/2 - b ==k:
            print(b)
            break