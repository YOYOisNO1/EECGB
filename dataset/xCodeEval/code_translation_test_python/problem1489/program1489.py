def program1489():
    l,r,x,y=map(int,input().split())
    if x==y:
        if x in range(l,r+1):
            print(1)
        else:
            print(0)
        exit(0)
    if y%x!=0:
        print(0)
        exit(0)
    m=y/x
    a=l//x
    if l%x!=0:
        a+=1
    b=r//x
    s=[]
    z=m
    k=2
    while z!=1:
        p=1
        while z%k==0:
            p*=k
            z/=k
        if p!=1 and p<=b:
            s.append(p)
        k+=1
    l=len(s)
    #print(s)
    if l==0:
        print(0)
        exit(0)
    c=0
    for i in range(pow(2,l-1)):
        p=1
        q=i
        for j in range(l):
            if q%2==1:
                p*=s[j]
            q//=2
        if p in range(a,b+1) and m/p in range(a,b+1):
            c+=2
    print(c)