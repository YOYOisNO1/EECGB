def program640():
    n,m=map(int,input().split())
    edges=[list(map(int,input().split())) for i in range(m)]
    for i in range(m):
        edges[i][0]-=1
        edges[i][1]-=1
    from itertools import permutations
    l=list(permutations(range(6)))
    mx=0
    for ij in l:
        for node in range(7):
            for seven in range(6):
                cnt=[None]*10
                for xi in range(6):
                    cnt[xi]=[0]*10
                    for xj in range(xi,6):
                        cnt[xi][xj]=1
                numbering=[0]*10
                c=0
                for i in range(6):
                    if node==i:
                        c=1
                    numbering[i+c]=ij[i]
                numbering[node]=seven
                curr=0
                for e in edges:
                    u,v=numbering[e[0]],numbering[e[1]]
                    u,v=min(u,v),max(u,v)
                    if cnt[u][v]:
                        cnt[u][v]=0
                        curr+=1
                mx=max(mx,curr)
    print(mx)