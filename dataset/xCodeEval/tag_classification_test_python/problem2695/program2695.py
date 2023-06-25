def program2695():
    import math
    a=list(map(int, input().split()))
    x=math.ceil((a[0]*8)/a[1]) +math.ceil((a[0]*5)/a[1])+math.ceil((a[0]*2)/a[1])
    print(x)