def numWays(n, k):
        if k == 0:
            return 0
    
        s = [1,1]
        for i in range(min(k-1, n-1)):
            s.append(s[-1] << 1)
    
        for i in range(n-k):
            s.append((s[-1] << 1) - s[i])
    
        return s[-1]
    
def solve():
        n, k, d = map(int, input().split())
        mod = 1_000_000_007
        print((numWays(n, k) - numWays(n, d-1)) % mod)
    
    if __name__ == '__main__':
        solve()
    