    N,K = map(int,input().split())
    A,B = map(int,input().split())
    
def gcd(a,b):
        if not a:
            return b
        if not b:
            return a
        return gcd(b,a%b)
    
    cur = 1+A
    nxt = []
    
    for i in range(N):
        nxt.append((1+i*K)-B)
        nxt.append((1+i*K)+B)
    
    ans = [0,10000000000]
    
    for i in nxt:
        L = i-cur
        if L > N*K or L < 0:
            L %= N*K
        if not L:
            L = N*K
        temp = gcd(L,N*K)
        ans[0] = max(ans[0],N*K/temp)
        ans[1] = min(ans[1],N*K/temp)
    
    print(ans[1],ans[0])