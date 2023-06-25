    import sys
    
    input = sys.stdin.readline
    
    MOD = 10 ** 9 + 7
    
    
    
    
def solve():
        n, k = list(map(int, input().split()))
        # c = [0] * (k + 1)
        # c[0] = 1
        # for i in range(k):
        #     c[i + 1] = (c[i] * (n - i)) // (i + 1)
        if k >= n:
            print(n)
            return
        cur = 1
        ans = 0
        for i in range(k + 1):
            ans += cur
            ans %= MOD
            cur = (cur * (n - i)) // (i + 1)
        print(ans)
    
    
    if __name__ == '__main__':
        solve()
    
    
    
    
     