    import sys
    input = sys.stdin.readline
    from collections import *
    
def bfs():
        q = deque([])
        dist = [-1]*(n*2*k)
        
        for i in range(2*k):
            q.append(i)
            dist[i] = 0
        
        while q:
            v = q.popleft()
            
            for nv in G[v]:
                if dist[nv]==-1:
                    dist[nv] = dist[v]+1
                    q.append(nv)
        
        for i in range(2*k):
            if dist[(n-1)*2*k+i]!=-1:
                return True
        
        return False
    
    for _ in range(int(input())):
        n, k, l = map(int, input().split())
        d = list(map(int, input().split()))
        G = [[] for _ in range(n*2*k)]
        p = [i for i in range(k+1)]+[i for i in range(k-1, 0, -1)]
        
        for i in range(n):
            for j in range(2*k):
                if d[i]+p[j]<=l and d[i]+p[(j+1)%(2*k)]<=l:
                    G[i*2*k+j].append(i*2*k+(j+1)%(2*k))
                
            if i+1<n:
                for j in range(2*k):
                    if d[i]+p[j]<=l and d[i+1]+p[(j+1)%(2*k)]<=l:
                        G[i*2*k+j].append((i+1)*2*k+(j+1)%(2*k))
        
        if bfs():
            print('Yes')
        else:
            print('No')