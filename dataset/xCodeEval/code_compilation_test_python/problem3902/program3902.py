def program3902():
    s, x1, x2 = [int(item) for item in input().split()]
    t1, t2 = [int(item) for item in input().split()]
    p, d = [int(item) for item in input().split()]
    v1, v2 = 1/t1,1/t2
    
    v2 *= int((x2 - x1)/(abs(x2 - x1)))
    
    x = x1
    c = int(v2/abs(v2))
    t = 0
    while p != x:
        t += 1
        p += d * v1
        if p == 0 or p == s:
            d *= -1
        x += v2
        if x == x2:
            print(t)
            break
    else:
        print(int(t + (x2 - x) / (v1 * d)))