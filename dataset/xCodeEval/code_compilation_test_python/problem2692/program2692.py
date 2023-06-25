def program2692():
    x=int(input())
    p=[1]*(x+1)
    a=2
    p[0]=0
    p[1]=0
    while a<=x:
        if p[a]:
            for i in range(a**2,x+1,a):
                p[i]=0
        a+=1
    c=[]
    for i in range(2,len(p)-1):
        if p[i]:
            c.append(i)
    for i in range(len(c)-1,-1,-1):
        if not x%c[i]:
            low=c[i]
            break
    poss=[i for i in range(x-low+1,x)]
    ans=poss[0]
    l=0
    r=1
    while poss[0]>=c[r+1]*2:
        r+=1
    for i in poss:
        while i-c[l]+1>=ans:
            l+=1
        if c[r]*2<=i:
            r+=1
        if l>r:
            break
        for j in range(l,r+1):
            if not i%c[j]:
                ans=min(ans,i-c[j]+1)
    print(ans)