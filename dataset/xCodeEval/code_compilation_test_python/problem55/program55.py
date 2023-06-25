def main():
        h, m, s, t1, t2 = [int(x) for x in input().split()]
        if h == 12:
            h = 0
        m += s/12
        h = h * 5 + m/12
        l = set([h, m, s])
    
        if t1 == 12:
            t1 = 0
        if t2 == 12:
            t2 = 0
        t1,t2 = t1*5, t2*5
        l = list(l) + [t1,t2]
        l.sort()
        if abs(l.index(t1) - l.index(t2)) == 1 or abs(l.index(t1) - l.index(t2)) == len(l) - 1:
            print("YES")
        else:
            print("NO")
    
    main()