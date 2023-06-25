def program719():
    from queue import Queue
    n,k=map(int,input().split())
    s=input()
    cost=0
    vis=set()
    q=Queue()
    q.put(s)
    while q:
        s=q.get()
        if s in vis: continue
        vis.add(s)
        cost+=len(s)
        if len(vis)==k: break
        for i in range(len(s)):
            q.put(s[:i]+s[i+1:])
    if len(vis)!=k: print(-1)
    else: print(n*k-cost)