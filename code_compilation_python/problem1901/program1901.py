    import sys
def main():
        x = []
        n,m = [int(i) for i in input().split()]
        a1,b1 = [int(i) for i in input().split()]
        a2,b2 = [int(i) for i in input().split()]
        ok = lambda a1,b1,a2,b2 : a1 + a2 <= x[0][0] and max(b1,b2)<= x[0][1] or b1 + b2 <= x[0][0] and max(a1,a2)<= x[0][1]
        print('YES' if ok(a1, c1, a2, c2) or ok(a1, c1, c2, a2) or ok(c1, a1, a2, c2) or ok(c1, a1, c2, a2) else 'NO')
    main()