def program4865():
    n,a,b=map(int,input().split())
    l=list(map(int,input().split()))
    r=list(reversed(l))
    c=0
    d=(n)//2
    for i in range(d):
        if l[i]==r[i]:
            if l[i]==2:
                c+=2*min(a,b)
        else:
            if (l[i]==0 and r[i]==1) or (l[i]==1 and r[i]==0):
                c=-1
                break
            else:
                if l[i]+r[i]==2:
                    c+=a
                else:
                    c+=b
    if n%2!=0:
        if l[d]==2 and c!=-1:
            c+=min(a,b)
    print(c)        