def numWays(n, k, mod):
        if k == 0:
            return 0
    
        s = [1,1]
        for i in range(min(k-1, n-1)):
            s.append((2*s[-1]) % mod)
    
        for i in range(n-k):
            s.append((((2*s[-1]) % mod) - s[i]) % mod)
    
        return s[-1]
    
def solve():
        n, k, d = map(int, input().split())
        mod = 1_000_000_007
        print((numWays(n, k, mod) - numWays(n, d-1, mod)) % mod)
    
    if __name__ == '__main__':
        solve()
    