def program221():
    n, k = list(map(int, input().split()))
    print(n+1+n+min(k-1+n-1,n-k+n-1))