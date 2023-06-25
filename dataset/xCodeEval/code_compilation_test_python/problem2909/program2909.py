    l,r,x,y=list(map(int, input().split() ) )
    if y%x!=0:
        print(0
    else:
    def dels(n):
            i=2
            p=[]
            while i*i<=n:
                while n%i==0:
                    p.append(i)
                    n=n//i
                i+=1
            if n>1:
                p.append(n)
            return p
        mins=dels(x)
        maxs=dels(y)
        d=dict()
        unique=list(set(maxs))
        for i in unique:
            d[i]=[mins.count(i), maxs.count(i) ]
        kol=len(d.keys())
        print(d)
        k=0
        for i in range(2**kol):
            dv=''
            while i!=0:
                dv+=str(i%2)
                i//=2
            dv=dv[::-1]
            if len(dv)<kol:
                dv='0'*(kol-len(dv))+dv
            a=1
            b=1
            for i in range(kol):
                if dv[i]=='1':
                    a*=unique[i]**  d[unique[i]][1]
                    b*=unique[i]**  d[unique[i]][0]
                else:
                    a*=unique[i]**  d[unique[i]][0]
                    b*=unique[i]**  d[unique[i]][1]
            if l<=a<=r and l<=b<=r and a!=b:
                k+=1
        print(k)