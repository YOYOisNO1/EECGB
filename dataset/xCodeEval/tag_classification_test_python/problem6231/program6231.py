def program6231():
    n,l=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    b1=False
    b2=False
    i=-1
    while i<l-1 and b1==False:
        i+=1
        for j in range(len(b)):
            b[j]+=1
            if b[j]>=l: b[j]-=l
        b.sort()
        b2 = False
        for j in range(n):
            if b[j]!=a[j]: b2=True
        if b2==False:
            b1=True
    if b1==False: print("NO")
    else: print("YES")