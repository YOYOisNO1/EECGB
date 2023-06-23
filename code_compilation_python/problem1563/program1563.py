def program1563():
    
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    Edges = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for a, b in Edges:
        adj[a].append(b)
        adj[b].append(a)
    if N <= 6:
        ans = M
    else:
        cnt = 100
        for i in range(7):
            for j in range(i+1, 7):
                cnt = min(cnt, len(adj[i] & adj[j]))
        ans = ans-cnt
    print(ans)