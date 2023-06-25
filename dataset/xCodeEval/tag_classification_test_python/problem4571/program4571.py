    #!/usr/bin/python3
    
    import functools
    
    @functools.lru_cache(maxsize = None)
def num(n):
        if n == 0:
            return 1
        if n == 1:
            return 2
        return num(n - 1) + num(n - 2)
         
    
    n = int(input())
    
    l, r = 0, 100
    while l < r - 1:
        mid = (l + r) >> 1;
        if (num(mid) <= n):
            l = mid
        else:
            r = mid
    
    print(l)
        