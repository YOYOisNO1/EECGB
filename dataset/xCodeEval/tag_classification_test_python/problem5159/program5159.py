    import math
    
def next_power_of_2(x):
        x += 1
        return 1 if x == 0 else 2**math.ceil(math.log2(x))
    
    
def value(n, l, r):
        if n == 1:
            return 1
    
        size = next_power_of_2(n)-1
        next_n = math.floor(n / 2)
        mid = math.floor(size/2)+1
    
        v = 0
        lv = 0
        rv = 0
        if l <= mid and mid <= r:
            v += n%2
        if l < mid:
            lv = value(next_n, l, min(mid-1, r))
        if r > mid:
            rv = value(next_n, max(1, l-mid), r-mid)
    
        v = v + lv + rv
    
    
        return v
    
def create(n):
        if n == 1:
            return [1]
        else:
            return create(math.floor(n/2))+ [n%2] + create(math.floor(n/2))
    
    
    [n, l, r] = [int(x) for x in input().split()]
    print(value(n,l,r))