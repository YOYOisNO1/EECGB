def program1052():
    # map(int, input().split())
    rw = 1 #int(input())
    for wewq in range(rw):
        n = int(input())
        a1, a2, a3 = map(int, input().split())
        b1, b2, b3 = map(int, input().split())
        a = [a1, a2, a3]
        b = [b1, b2, b3]
        f = 0
        t = min(a1, b2)
        f += t
        a1 -= t
        b2 -= t
        t = min(a2, b3)
        f += t
        a2 -= t
        b3 -= t
        t = min(a3, b1)
        f += t
        a3 -= t
        b1 -= t
        wins = f
        #------------------------------#
        a1, a2, a3 = a
        b1, b2, b3 = b
        #------------------------------#
        f = 0
        d1 = a1 - b1
        d2 = a2 - b2
        d3 = a3 - b3
        if d1 < 0 - a2:
            f += -d1 - a2
            a1 = 0
            a2 = 0
        d2 = a2 - b2
        d3 = a3 - b3
        if d2 < 0 - a3:
            f += -d2 - a3
            a2 = 0
            a3 = 0
        d3 = a3 - b3
        if d3 < 0 - a1:
            f += -d3 - a1
        #------------------------------#
        print(f, wins)