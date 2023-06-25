def program988():
    #1426E
    from itertools import permutations 
    import sys
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    maxa=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    combi=((0,0),(1,1),(2,2),(0,2),(1,0),(2,1))
    mina=sys.maxsize
    for i in permutations((combi)):
        a1=a[:];b1=b[:]
        for j in i:
            x=min(a1[j[0]],b1[j[1]])
            a1[j[0]]-=x
            b1[j[1]]-=x
        mina=min(mina,min(a1[0],b1[1])+min(a1[1],b1[2])+min(a1[2],b1[0]))
    print("%d %d" %(mina, maxa))