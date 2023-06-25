    import sys
    input = sys.stdin.readline
    
def solve():
        n,m = map(int,input().split())
    
        cnt = [0]*20
        vis = [0]*(20*m + 1)
    
        c = 0
        for k in range(1, 20):
            for j in range(1,m+1):
                if not vis[k*j]:
                    c += 1
                    vis[k*j] = 1
            cnt[k] = c
    
        seen = [False]*(n+1)
        ans = 1
        for i in range(2,n+1):
            if seen[i]:
                continue
    
            ii = i
            k = 0
            while ii <= n:
                seen[ii] = True
                ii *= i
                k += 1
    
            ans += cnt[k]
    
        print(ans)
    
    
    for nt in range(1):
        solve()