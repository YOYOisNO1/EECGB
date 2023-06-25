    #!/usr/bin/python
    import sys
def egcd(a, b):
        x1, x2, y1, y2, r1, r2 = 1, 0, 0, 1, a, b
        while r1 != 0:
            q = r2 / r1
            r2, r1 = r1, r2%r1
            x2, x1 = x1, x2-(q*x1)
            y2, y1 = y1, y2-(q*y1)
        return r2, x2, y2
    
def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a
    
def crt(A, M):
        a, m = A[0], M[0]
        for i in range(1,len(A)):
            g, x, Y = egcd(m, M[i])
            if (a - A[i])%g != 0:
                return None
            lcm = m / g * M[i]
            a = (a*M[i]*Y + A[i]*m*x)/g%lcm
            m = lcm
        return a
    
def solve():
        n,m,x,y,vx,vy = map(int, input().split())
        if vx == 0:
            if (x != 0 and x != n): return -1
            return '%d %d'%(x, m if vy == 1 else 0)
        elif vy == 0:
            if (y != 0 and y != m): return -1
            return '%d %d'%(n if vx == 1 else 0, y)
    
        t = crt([-x/vx, -y/vy], [n,m])
    
        if t is None or (x+vx*t)%n != 0 or (y+vy*t)%m != 0:
            return -1
    
        fx = n if (x+vx*t)/n%2 == 1 else 0
        fy = m if (y+vy*t)/m%2 == 1 else 0
        return '%d %d'%(fx,fy)
    
    print(solve())