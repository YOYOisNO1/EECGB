    import sys
    
    n = int(input())
    
    x = [0]*n
    y = [0]*n
    
    sx = 0
    sy = 0
    
    for i in range(n):
        x[i], y[i] = map(int, input().split())
        sx += x[i]
        sy += y[i]
        
    for i in range(n):
        x[i] = n * x[i] - sx
        y[i] = n * y[i] - sy
    
    m = int(input())
    
    d = [0]*n
    e = [0]*n
    
def check(a, b):
        global d, e
        for i in range(n):
            e[i] = (a-x[i])*(a-x[i])+(b-y[i])*(b-y[i])
        e.sort()
        return d == e
    
def sqrt(x):
        nn = int(x)
        if nn == 0:
            return 0
        fa, fb = divmod(nn.bit_length(), 2)
        x = 2**(fa+fb)
        while True:
            y = (x + nn//x)//2
            if y >= x:
                return x
            x = y
    
def solve():
        global d
        d = list(map(int, input().split()))
        c = 0
        d = [p * n * n for p in d]
        for i in range(n):
            c += d[i] - x[i] * x[i] - y[i] * y[i]
    
        assert(c % n == 0)
        c //= n
        ans = []
        ax = x[0]
        ay = y[0]
        if ax is 0 and ay is 0:
            ax = x[1]
            ay = y[1]
        d.sort()
        old = -1
        for p in d:
            if (p == old):
                continue
            old = p
            a = c + ax * ax + ay * ay - p
            if (a % 2 != 0):
                continue
            a //= 2
            A = ax * ax + ay * ay
            B = a * ax
            C = a * a - ay * ay * c
            D = B * B - A * C
            if (D < 0):
                continue
            sD = sqrt(D)
            if D != sD * sD:
                continue
            if (B + sD) % A == 0:
                qx = (B + sD) // A
                qy = (a - ax * qx) // ay
                if ((qx + sx) % n == 0 and (qy + sy) % n == 0 and check(qx, qy)):
                    qx = (qx + sx) // n
                    qy = (qy + sy) // n
                    ans.append([qx, qy])
            if sD == 0:
                continue
            if (B - sD) % A == 0:
                qx = (B - sD) // A
                qy = (a - ax * qx) // ay
                if ((qx + sx) % n == 0 and (qy + sy) % n == 0 and check(qx, qy)):
                    qx = (qx + sx) // n
                    qy = (qy + sy) // n
                    ans.append([qx, qy])
                    
        ans.sort()
        print(len(ans), end = ' ')
        for p in ans:
            print(p[0], p[1], end = ' ')
        print()
    
    while m > 0:
        m -= 1
        solve()
           