def program1137():
    from math import ceil
    n, m, k = map(int, input().split())
    x = ceil(k/(2*m))
    if k % (2 * m):
        y = ceil((k%(2*m))/2)
    else: y = m
    z = 'L' if k%2 else 'R'
    print(x, y, z)