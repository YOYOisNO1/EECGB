    import sys
    
def readnum():
        input = sys.stdin.readline
        a=list(map(int,input().split()))
        return a
    
def printf(val):
        sys.stdout.write(str(val) + '\n')
    
def power(a, b, mod):
        if b == 1:
            return a
        if b == 0:
            return 1
    
        ans = power(a, b//2, mod)
        ans *= ans
    
        if b % 2:
            ans *= a
        
        ans = ans % mod
        return ans
    
    t = readnum()[0]
    
    for _ in range(t):
        n, k = readnum()
        print((power(n,) k, 10**9 + 7))