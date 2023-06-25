    from math import log, floor
    
def binarysearch(x, n, k, p):
        left = 0
        right = len(x)
        while left < right:
            middle = (left + right) // 2
            if sum([x[middle]//k**i for i in range(p+1)]) < n:
                left = middle + 1
            else:
                right = middle
        
        return left
    
    n, k = [int(i) for i in input().split()]
    p = floor(log(n, k))
    x = list(range(n//2, n+1))
    y = binarysearch(x, n, k, p)
    
    print(x[y])