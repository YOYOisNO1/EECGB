def program4961():
    import sys
    range = xrange
    input = input
    
    inp = [int(x) for x in sys.stdin.read().split()]; ii = 0
    
    n = inp[ii]; ii += 1
    coupl = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = inp[ii] - 1; ii += 1
        v = inp[ii] - 1; ii += 1
        coupl[u].append(v)
        coupl[v].append(u)
    
    P = [-1] * n
    root = 0
    bfs = [root]
    P[root] = root
    for node in bfs:
        for nei in coupl[node]:
            del coupl[nei][coupl[nei].index(node)]
            bfs.append(nei)
            P[nei] = node
    
    ans = [-1] * n
    
    cost = - 2 * n
    
    houses = [[i] for i in range(n)]
    people = [[i] for i in range(n)]
    for node in reversed(bfs):
        H = houses[node]
        Pe = people[node]
    
        cost += len(H) + len(Pe)
    
        Pe.reverse()
        if len(H) > 1 or len(Pe) > 1:
            while H and Pe:
                house = H.pop()
                p = Pe.pop()
                ans[house] = p
    
        houses[P[node]] += H
        people[P[node]] += reversed(Pe)
    
    print cost
    print ' '.join(str(x + 1) for x in ans)