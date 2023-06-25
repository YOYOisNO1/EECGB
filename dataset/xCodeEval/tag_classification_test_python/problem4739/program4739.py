def program4739():
    from math import ceil, sqrt
    
    n, m = [int(i) for i in input().split()]
    
    if m >= n:
        print(n)
    
    
    else :
        l = 0
        r = 10**18
        ans = 10**18
        while (l <= r):
            mid = (l + r) // 2
    
            if mid * mid + mid >= 2 * (n - m):
                ans = mid
                r = mid - 1
    
            else:
                l = mid + 1
    
        print(ans + m)