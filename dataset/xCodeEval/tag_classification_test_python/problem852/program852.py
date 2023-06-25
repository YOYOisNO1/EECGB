def coff(n,k):
        c=[[0 for x in range(k+1)] for x in range(n+1)]
        for i in range(n+1):
            for j in range(min(i,k)+1):
                if j==0 or j==i:
                    c[i][j]=1
                else:
                    c[i][j]=c[i-1][j-1]+c[i-1][j]
        return c[n][k]
    s1=input()
    s2=input()
    p1=0
    n1=0
    for i in s1:
        if i=='+':
            p1+=1
        else:
            n1+=1
    p2=0
    n2=0
    q=0
    for i in s2:
        if i=='+':
            p2+=1
        elif i=='-':
            n2+=1
        else:
            q+=1
    if q==0:
        if p1==p2 and n1==n2:
            print(round(1/1,10))
        else:
            print(round(0/1,10))
    else:
        p=p1-p2
        n=n1-n2
        #print(p,n,n1,n2)
        if p<0 and n<0:
            print(round(0/1,10))
        elif p<0 and n>0:
            n+=abs(p)
            if n!=q:
                print(round(0/1,10))
            else:
                print(round(1/2**n,10))
        elif p>0 and n<0:
            p+=abs(n)
            if p!=q:
                print(round(0/1,10))
            else:
                print(round(1/2**p,10))
        else:
            if p+n!=q:
                print(round(0/1,10))
            else:
                #print(p,n)
                #x=['+' for i in range(p)]+['-' for i in range(n)]
                if p==0:
                    perm=1
                elif n==0:
                    perm=1
                else:
                    perm=coff(q,p)*coff(q-p,n)
                #print(coff(q,p),coff(q-p,n))
                #perm=coff(q,p)+coff(q-p,n)
                #print(perm)
                print(round(perm/2**q,10))