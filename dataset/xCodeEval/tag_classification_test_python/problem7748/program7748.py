    from sys import stdin
    
    
def bs():
        be, en = 1, k + 1
    
        while be < en:
            mid = (be + en + 1) >> 1
            be1, cur = (mid + m - 1) // m, 0
    
            for i in range(1, be1):
                cur += m
    
            for i in range(be1, n + 1):
                cur += (mid - 1) // i
    
            if cur <= k - 1:
                be = mid
            else:
                en = mid - 1
    
        print(be)
    
    
    n, m, k = [int(x) for x in stdin.readline().split()]
    bs()