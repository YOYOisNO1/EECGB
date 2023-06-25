def program2508():
    n,m=map(int,input().split())
    v=0
    for b in sorted((list(map(int,input().split())))[::-1] for i in range(m), reverse=True):
        c=min(b[1],n)
        n-=c
        v+=c*b[0]
    print(v)    