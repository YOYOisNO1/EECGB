def program3850():
    
    import sys
    #sys.stdin=open("data.txt")
    input=sys.stdin.readline
    
    n=int(input())
    d=list(map(int,input().split()))
    
    t1=[1000]*n     # rest
    t2=[1000]*n     # activity 1
    t3=[1000]*n     # activity 2
    
    t1[0]=1
    if d[0]&1: t2[0]=0
    if d[0]&2: t3[0]=0
    
    for i in range(n-1):
        t1[i+1]=min(t1[i],t2[i],t3[i])+1
        if d[i+1]&1: t2[i+1]=min(t1[i],t3[i])
        if d[i+1]&2: t3[i+1]=min(t1[i],t2[i])
    
    print(min(t1[-1],t2[-1],t3[-1]))