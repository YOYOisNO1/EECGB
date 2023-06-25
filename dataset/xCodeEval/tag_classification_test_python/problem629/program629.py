def program629():
    n=int(input())
    b=input()
    a,c,d,e=[],[],[],[]
    nom=0
    maxx=0
    bb=0
    for i in range(n):
        a.append(b[i])
        if a[i].islower()==True:
            c.append('m')
        else:
            c.append('b')
    #print(c)
    for i in range(n):
        if c[i]=='b':
            d.append(i)
    if 0 not in d:
        d.insert(0,0)
    if c[n-1]!='b':
        d.append(n)
    #print(d)
    #print(c)
    if 'm' not in c:
        print(0)
    else:
        for i in range(len(d)-1):
            e.append([])
            for j in range(d[i],d[i+1]):
                if c[j]=='b':
                    j+=1
                if b[j] not in e[nom]:
                    e[nom].append(b[j])
            #print(e)
            nom+=1
        for i in range(len(e)):
            if len(e[i])>maxx:
                maxx=len(e[i])
        print(maxx)