def L(h, n):
        if h == 0:
            return 0
        half = 2**(h-1)
        if n <= half:
            return 1 + R(h-1, n)
        else:
            return 2*half + L(h-1, n-half)
    
def R(h, n):
        if h == 0:
            return 0
        half = 2**(h-1)
        if n <= half:
            return 2*half + R(h-1, n)
        else:
            return 1 + L(h-1, n-half)
    
    [h, n] = map(int, input().split(" "))
    print(L(h,) n)