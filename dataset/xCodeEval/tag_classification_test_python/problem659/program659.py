def program659():
    import math
    n, m=map(int, input().split())
    a=int(math.ceil(math.sqrt(m*2)))
    print(max(n-m*2,) 0), n-a if a*(a-1)/2>=m else n-a-1