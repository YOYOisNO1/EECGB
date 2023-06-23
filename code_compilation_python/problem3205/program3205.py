def program3205():
    n,h,m = list(map(int, input().split()))
    arr = n*[h]
    # print()
    # print(arr)
    for i in range(m):
        l,r,x = list(map(int, input().split()))
        # it = l 
        for j in range(len(arr)):
            if j >= l-1 and j <= r-1:
                if arr[j] > x:
                    arr[j] = x
        # print(arr)
    ans = 0
    for k in arr:
        ans += (k**2) 
    print(ans)