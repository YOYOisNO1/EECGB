    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    dp = [[0] * (1 << n) for _ in range(1 << n)]
    
    for u, v in (map(int, input().split()) for _ in range(m)):
        u, v = u - 1, v - 1
        adj[u].append(v)
        adj[v].append(u)
        dp[(1 << u) | (1 << v)][(1 << u) | (1 << v)] = 1
    
    
    for v_set in range(1, 1 << n):
        leaf_set = v_set
    
        while leaf_set:
            for new_v in range(n):
                if (1 << new_v) & v_set:
                    continue
                for bridge in adj[new_v]:
                    if (1 << bridge) & v_set == 0:
                        continue
                    new_leaf_set = (leaf_set | (1 << new_v)) & ~(1 << bridge)
    
                    if (((1 << new_v) - 1) & new_leaf_set) == 0:
                        dp[v_set | (1 << new_v)][new_leaf_set] += dp[v_set][leaf_set]
    
            leaf_set = (leaf_set - 1) & v_set
    
    ans = 0
    bit = (1 << k) - 1
    while bit < (1 << n):
        ans += dp[-1][bit]
        x = bit & -bit
        y = bit + x
        bit = (((bit & ~y) // x) >> 1) | y
    
    print(ans)