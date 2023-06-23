def program2796():
    # arr=list(map(int,input().split()))
    # arr=sorted([(n-int(x),i) for i,x in enumerate(input().split())])
    # arr=[int(q)-1 for q in input().split()]
    # from collections import Counter
    # n=int(input())
    # n,k=map(int,input().split())
    # arr=list(map(int,input().split()))
    # for i in range(m):
    #for _ in range(int(input())):
    #n=int(input())
    
    l,d,v,g,r=map(int,input().split())
    t1=d/v
    #print(t1)
    slot=t1//(r+g)
    t1=t1-slot*(r+g)
    if t1<=g:
        wait=0
    else:
        wait=(r+g)-t1
    
    #print(wait)
    total=wait+l/v
    print("%.8f"%total)