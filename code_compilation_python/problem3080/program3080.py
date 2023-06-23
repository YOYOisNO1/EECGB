def program3080():
    import math
    c = map(int, input.split())
    a = c[0]
    b = c[1]
    if a == b:
        print 0
    else:
        d = a ^ b
        e = math.log(d, 2) + 1
        print 2**int(e) - 1
        