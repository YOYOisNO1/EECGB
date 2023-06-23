def program2177():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    
    for k in range(0,n):
        total = 0
        grps = (k+n-1)//n
        for i in range(n):
            total += max(0, arr[i] - i%grps)
        if total>=m:
            print(k)
    print(-1)