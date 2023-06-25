def program2522():
    from math import pow
    from math import trunc
    import math
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        l = 0 
        r = n
        three = 0
        while l < r:
            mid = (l + r) // 2
            if mid ** 3 <= n:
                l = mid + 1
            else:
                r = mid
        three = r
        l = 0 
        r = n
        six = 0
        while l < r:
            mid = (l + r) // 2
            if mid ** 6 <= n:
                l = mid + 1
            else:
                r = mid
        six = r
        ans = trunc(pow(n, 0.5)) +  three - six
        print(ans)