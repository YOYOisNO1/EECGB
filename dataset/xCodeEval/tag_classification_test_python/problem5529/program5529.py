def program5529():
    n, k = map(int,input().strip().split())
    arr = map(int,input().strip().split())
    if len(filter(lambda x:x>k,arr))==0:
        print(n)
    else:
        left = 0
        while left<n and arr[left]<=k:
            left += 1
        right = n-1
        while right>=0 and arr[right]<=k:
            right -= 1
        ans = left + (n-right-1)
        print(ans)
    