    import sys
    sys.stderr = sys.stdout
    
def egcd(a, b):
        r0 = a
        r1 = b
        s0 = 1
        s1 = 0
        t0 = 0
        t1 = 1
        while r1:
            q = r0 // r1
            r0, r1 = r1, r0 - q*r1
            s0, s1 = s1, s0 - q*s1
            t0, t1 = t1, t0 - q*t1
        return r0, s0
    
    
def app(n, M):
        K = [[[1]]]
        for i in range(n-1):
            Ki = K[i]
            ni = len(Ki)
            Ki_ = [[0] * (i+2) for _ in range(ni + i + 1)]
            K.append(Ki_)
            for j, Kij in enumerate(Ki):
                for k, v in enumerate(Kij):
                    for h in range(i+1):
                        Ki_[j+h][k] += v
                        Ki_[j+h][k] %= M
                    Ki_[j + i + 1][i+1] += v
                    Ki_[j + i + 1][i+1] %= M
    
        c = n
        s = 0
        for i in range(1, n):
            Ki = K[i]
            ni = len(Ki)
            mi = len(Ki[0])
            Si = [[None] * mi for _ in range(ni)]
            for j in range(ni):
                Si[j][mi-1] = Ki[j][mi-1]
                for k in reversed(range(mi-1)):
                    Si[j][k] = (Ki[j][k] + Si[j][k+1]) % M
            for j in range(1, ni):
                for k in range(mi):
                    Si[j][k] += Si[j-1][k]
                    Si[j][k] %= M
            # log("i", i, "Ki", Ki, "Si", Si)
    
            si = 0
            for j in range(1, ni):
                for k in range(mi-1):
                    si += (Ki[j][k] * Si[j-1][k+1]) % M
                    si %= M
            # log("  si", si)
    
            # log("  n", n, "i+1", i+1, "c", c)
            x, y = egcd(i+1, M)
            c = (c * y) % M
            # log("  x", x, "y", y)
            # assert c % x == 0
            c = (c // x) % M
            c = (c * (n - i)) % M
            # log("  c", c)
    
            si *= c
            si %= M
            s += si
            s %= M
    
        return s
    
    
def main():
        n, m = readinti()
        print(app(n, m))
    
    ##########
    
def readint():
        return int(input())
    
    
def readinti():
       return map(int, input().split())
    
    
def readintt():
       return tuple(readinti())
    
    
def readintl():
       return list(readinti())
    
    
def readinttl(k):
        return [readintt() for _ in range(k)]
    
    
def readintll(k):
        return [readintl() for _ in range(k)]
    
    
def log(*args, **kwargs):
        print(*args, **kwargs, file=sys.__stderr__)
    
    
    if __name__ == '__main__':
        main()