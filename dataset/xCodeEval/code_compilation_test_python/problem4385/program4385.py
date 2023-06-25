def program4385():
    from time import*
    n=6#{int(input())
    t=time()
    p2=1
    v=0
    while p2*2<=n:
        p2*=2
        v+=1
    mo=10**9+7
    tr=[n//(2**k) for k in range(v+1)]
    tabn=[0]*(v+1)
    tabn[-2]=tr[-2]-1
    for k in range(2,n):
        if tr[v-1]<k-2:
            v-=1
        tab=tabn[:]
        tabn=[0]*(v+1)
        for j in range(v):
            tabn[j]=(max((tr[j]-k),0)*tab[j]+(tr[j]-tr[j+1])*tab[j+1])%mo
    s=tabn[0]
    p2=1
    v=0
    while p2*2<=n:
        p2*=2
        v+=1
    tr=[n//(3*2**k) for k in range(v+1)]
    tr3=[n//(2**k) for k in range(v+1)]
    tab3n=[0]*(v+1)
    tabn=[0]*(v+1)
    tabn[-2]=tr[-2]#3*2**k-1
    for k in range(1,n):
        if tr3[v-1]<k-2:
            v-=1
        tab=tabn[:]
        tabn=[0]*(v+1)
        tab3=tab3n[:]
        tab3n=[0]*(v+1)
        for j in range(v):
            tabn[j]=(max((tr[j]-k),0)*tab[j]+(tr[j]-tr[j+1])*tab[j+1])%mo
        for j in range(v):
            tab3n[j]=(max((tr3[j]-k),0)*tab3[j]+(tr3[j]-tr3[j+1])*tab3[j+1]+(tr3[j]-tr[j])*tab[j])%mo
    print((s+tab3n[0])%mo)