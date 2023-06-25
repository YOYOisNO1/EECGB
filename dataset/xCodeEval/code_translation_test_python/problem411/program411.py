def program411():
    s, x1, x2 = map(int, input().strip().split())
    t1, t2 = map(int, input().strip().split())
    p, d = map(int, input().strip().split())
    ans = abs(x2-x1)*t2
    if t1 < t2:
        u = (x2-p)/abs(x2-p)    
        v = (x2-x1)/abs(x2-x1)
        t = 0
        if u == d:
            y = d*(x2-p)
            t = t1*y
            if d == v:
                if y >= (x2-x1)*v:
                    ans = min(ans, t)
                else:
                    y = 2*(x2 if d < 0 else (s-x2))
                    t += t1*y
                    d *= -1
        else:
            y = abs(x2-p) + 2*(p if d < 0 else (s-p))
            t = t1* y
            d *= -1
            if d == v: ans = min(ans, t)
        while d != v:
            y = 2*(x2 if d < 0 else (s-x2))
            t += t1*y
            # print("next t=%d") % t
            ans = min(ans, t)
            d *= -1
    print(ans)
    
    
    
    