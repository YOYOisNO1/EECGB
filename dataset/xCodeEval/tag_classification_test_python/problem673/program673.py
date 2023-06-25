    from fractions import *
    
def binarySearch(a, b, x, y):
        s = 0
        e = 10**18
        it = 80
        while it:
            it -= 1
            mid = (s + e) >> 1
            if (x * mid <= a) and (y * mid <= b):
                s = mid
            else:
                e = mid
        s = mid - 5
        if s < 0:
            s = 0
        e = mid + 5
        res = 0
        while s <= e:
            if (x * s <= a) and (y * s <= b):
                res = s
            s += 1
        return res
    
    a, b, x, y = map(int, input().split())
    
    g = gcd(x, y)
    x /= g
    y /= g
    
    print(binarySearch(a,) b, x, y)