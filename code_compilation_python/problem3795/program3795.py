def program3795():
    n, m, a, b = map(int, input().split())
    n -= 1
    a -= 1
    b -= 1
    ax = a%m
    ay = a/m
    bx = b%m
    by = b/m
    if (ay == by) or ((ax == 0) and (b == n)) or ((ax == 0) and (bx == m-1)):
        print 1
    elif (ay+1 == by) or (ax == 0) or (bx == m-1) or (b == n) or (ax-1 == bx):
        print 2
    else:
        print 3