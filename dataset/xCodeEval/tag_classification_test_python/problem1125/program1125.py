def main():
        n = int(input())
        r2, s2, p2 = map(int, input().split())
        r1, s1, p1 = map(int, input().split())
    
        ma = min(r1, p2)+min(s1, r2)+min(p1, s2)
        if s2>=r1+s1:
            mi = s2-r1-s1
            #print("a", mi)
        else:
            mi = n
            k1 = max(0, s2-s1)
            k2 = min(r1, s2)
            #print(k1, k2)
            c1 = r1-r2
            c2 = p2-s1+s2
            if k1<=c1:
                mi = c1-min(k2, c1)
                #print(1, mi)
            if k2>=c2:
                mi = min(mi, max(k1, c2)-c2)
                #print(2, mi)
            if c2>c1+1 and (c2>k1 and c1<k2) or (k1>c1 and k2<c2):
                mi = 0
        print(mi, ma)
    main()