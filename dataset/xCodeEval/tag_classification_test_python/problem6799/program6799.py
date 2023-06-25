    import sys
    
    I = lambda: int(input())
    RL = readline = lambda: sys.stdin.readline().strip('\n')
    RM = readmap  = lambda x = int: map(x,readline().split(' '))
    
    k,s = I(),list(RL());n=len(s);n1 = n-1;ss = set(s)
    alpha = {chr(97+i) for i in range(k)}
    alpha0 = [chr(97+i) for i in range(k)]
    alpha0 = [i for i in alpha0 if not i in ss]
def discard(l,x):
        if x in l: l.remove(x)
    
    if n&1 and s[n>>1] == '?': s[n>>1] = (alpha0.pop() if len(alpha0) else 'a')
    for i in range((n>>1)-1,-1,-1):
        x,y = s[i],s[n1-i]
        flag = max(ord(x)-96,ord(y)-96)>k
        c = int(x=='?') + int(y=='?')
        if c==0:
            if x!=y: flag = True
            else: discard(alpha0,x)
        if c==2: s[i] = s[n1-i] = (alpha0.pop() if len(alpha0) else 'a')
        if c==1:
            if x=='?': s[i]    = y;discard(alpha0,y)
            if y=='?': s[n1-i] = x;discard(alpha0,x)
        if flag:
             print('IMPOSSIBLE');sys.exit(0)
    
    #print(alpha0,alpha,set(s))
    print(''.join(s) if set(s)==alpha else "IMPOSSIBLE")
    quit()
    '''
    16
    ?bc??f?hi?k??n??hb??liiglal???npi???b???p?n?j?al????j???ponmlkjih??e??b?
    '''
    #D 
def f(l,x):
        if x==l[0]: return l[1],l[2]
        if x==l[1]: return l[0],l[2]
        if x==l[2]: return l[0],l[1]
        return -1
    
def delrank(x):
        global pre,nxt
        prex,nxtx = pre[x],nxt[x]
        nxt[prex] = nxtx
        pre[nxtx] = prex
    
    n = I()
    N = 3*n
    rank = [*RM()]+[N+1]
    tris = [tuple(RM()) for i in range(n)]
    k    = I()
    pre,nxt = list(range(N+2)), list(range(N+2))
    temp0 = 0
    for i in range(N+1):
        temp1 = rank[i]
        pre[temp1],nxt[temp0] = temp0,temp1
        temp0 = temp1
    
    for ind,tri in enumerate(tris):
        leader = nxt[0]
        x,y = f(tri,leader)
        if k in tri:
            if leader != k:
                l = [i for i in range(1,N+1) if i!=k]
            else:
                #condition here is element in l3 should be after max(x,y)
                #so sort l1+l2 first cut the portion after max(x,y) and add
                #it to l3 and sort the new l3
                l1 = [i for tri in tris[:ind] for i in tri]
                l2 = [x,y]
                l3 = [i for tri in tris[ind+1:] for i in tri]
                l0 = sorted(l1 + l2)
                ind = l0.index(max(x,y))
                l = l0[:ind+1] + sorted(l0[ind+1:]+l3)
                #print(leader,l1,l2,l3)
            print(' '.join([str(i) for i in l]))
            sys.exit(0)
        for i in tri: delrank(i)
    
    '''
    7
    4 19 14 8 21 16 2 18 1 15 3 17 13 5 6 10 9 7 12 11 20
    4 19 10
    14 8 3
    21 17 9
    16 6 12
    2 13 20
    18 1 7
    15 5 11
    21
    '''
    quit()
    #E  Shortest Path
def rec(u,v):
        '''to recursivley visit the edge previous to this edge'''
        if v:  rec(pre[u][v],u);print(v,end=' ')
    
    from collections import deque
    n,m,k = RM()
    adj  = [[] for i in range(n+1)]
    dist = [[int(1e9)]*(n+1) for i in range(n+1)]
    pre  = [[0]*(n+1)        for i in range(n+1)]
    bad  = set()
    for _ in range(m):
        x,y = RM()
        adj[x].append(y)
        adj[y].append(x)
    
    for _ in range(k):  bad.add(tuple(RM()))
    
    dist[0][1] = 0
    q = deque([(0,1)])
    while q:
        u,v = q.popleft()
        d   = dist[u][v] + 1
        for w in adj[v]:
            if d<dist[v][w] and  not (u,v,w) in bad:
                dist[v][w] = d
                pre[v][w] = u
                q.append((v,w))
                if w == n:
                    print(d)
                    rec(v,w)
                    print()
                    sys.exit(0)
    print(-1)