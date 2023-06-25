    #!/usr/bin/env python3
    from sys import stdin
    
    
def solve(tc):
        n, a, b = map(int, stdin.readline().split())
    
        if a*b >= 6*n:
            print(a*b)
            print(a, b)
            return
    
        mini = int(1e18)+1
        minv = (-1, -1)
        if a > b:
            a, b = b, a
    
        base = 6 * n
        ma = a
        while True:
            if base//ma < b:
                break
    
            if base % ma == 0:
                print(base)
                print(ma, base//ma)
                return
    
            mb = base // ma + 1
            if mini > ma*mb - base:
                mini = ma*mb - base
                minv = (ma, mb)
    
            ma += 1
    
        print(minv[0]*minv[1])
        print(minv[0], minv[1])
    
    
    tc = 1
    solve(tc)