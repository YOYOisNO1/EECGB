def f(n):
        res = n
        while n != 0:
            res -= n % 10
            n /= 10
        return res
    
    
    
    n,s = input().split(" ")
    
    l = 1
    d = n
    
    if f(n) < s:
        print "0"
        return
    
    while l < d:
        mid = l + (d - l)/2
        if f(mid) >= s:
            d = mid
        else:
            l = mid + 1
    
    print n - l + 1
    
        