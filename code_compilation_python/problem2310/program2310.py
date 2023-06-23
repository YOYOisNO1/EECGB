def program2310():
    ef f():
        r1, r2 = map(int, input().split())
        c1, c2 = map(int, input().split())
        d1, d2 = map(int, input().split())
    
        a = r1 + d1 - c2
        if a % 2: print(-1)
        else:
            a = a // 2
            b = r1 - a
            d = d1 - a
            c = r2 - d
    
            if c1 != a + c or c2 != b + d or d2 != b + c or len(set([a, b, c, d])) < 4: print(-1)
            else:
                print(a, b)
                print(c, d)
    
    f()