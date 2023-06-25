    import sys
    inf=sys.maxsize
    
def max_flow(C, s, t):
            n = len(C)
            F = [[0] * n for i in range(n)]
            path = bfs(C, F, s, t)
    
            while path != None:
                flow = min(C[u][v] - F[u][v] for u,v in path)
                for u,v in path:
                    F[u][v] += flow
                    F[v][u] -= flow
                path = bfs(C, F, s, t)
            return sum(F[s][i] for i in range(n))
    
def bfs(C, F, s, t):
            queue = [s]
            paths = {s:[]}
            if s == t:
                return paths[s]
            while queue:
                u = queue.pop(0)
                for v in range(len(C)):
                        if(C[u][v]-F[u][v]>0) and v not in paths:
                            paths[v] = paths[u]+[(u,v)]
                            if v == t:
                                return paths[v]
                            queue.append(v)
            return None
    
    n=int(input())
    r1,s1,p1=map(int,input().split())
    r2,s2,p2=map(int,input().split())
    
    g=[]
    g.append([0,r1,s1,p1,0,0,0,0])
    g.append([0,0,0,0,r2,0,p2,0])
    g.append([0,0,0,0,r2,s2,0,0])
    g.append([0,0,0,0,0,s2,p2,0])
    g.append([0,0,0,0,0,0,0,inf])
    g.append([0,0,0,0,0,0,0,inf])
    g.append([0,0,0,0,0,0,0,inf])
    g.append([0,0,0,0,0,0,0,0])
    
    source=0
    sink=7
    max_flow_value = max_flow(g,source,sink)
    
    mi=n-max_flow_value
    ma=min(r1,s2)+min(s1,p2)+min(p1,r2)
    
    print(mi,ma)