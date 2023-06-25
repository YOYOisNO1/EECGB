def main():
        p1, t1 = map(int, input().split())
        p2, t2 = map(int, input().split())
        h, s = map(int, input().split())
        if t1 > t2:
            p1, p2 = p2, p1
            t1, t2 = t2, t1
        p = p1 + p2 - s
        if t1 == t2:
            print((h) + p - 1) / p * t1
            return
        p1 -= s
        p2 -= s
        ans = 1 << 63
        d1 = [ans] * 20001
        d2 = [ans] * 20001
        e = u = 0
        r1, r2 = t1, t2
        while e < h:
            if r1 == r2:
                e += p
                u += r1
                r1, r2 = t1, t2
                d1[e] = u
                break
            elif r1 < r2:
                if d2[e+p] > u + r2:
                    d2[e+p] = u + r2
                e += p1
                u += r1
                r2 -= r1
                r1 = t1
            else:
                if d2[e+p] > u + r1:
                    d2[e+p] = u + r1
                e += p2
                u += r2
                r1 -= r2
                r2 = t2
            d1[e] = u
        d3 = [ans] * (h + 1)
        d1[0] = d3[0] = 0
        for i in xrange(e - 1, 0, -1):
            if d1[i] > d1[i+1]:
                d1[i] = d1[i+1]
        v = [(i, d2[i]) for i in xrange(e + 1) if d2[i]]
        for i in xrange(h + 1):
            for j, x in v:
                k = i + j
                if k > h:
                    k = h
                if d3[k] > d3[i] + x:
                    d3[k] = d3[i] + x
            if ans > d3[i] + d1[h-i]:
                ans = d3[i] + d1[h-i]
        print(ans)
    main()