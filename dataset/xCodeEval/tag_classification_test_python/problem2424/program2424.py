def program2424():
    a=int(input())
    b=input()
    c=b
    ip=[]
    op=[]
    nip=0
    while len(c):
        if c[0]=='_':
            c=c[1:]
        elif c[0]=='(':
            ind=c.find(')')
            ip.append(c[1:ind])
            c=c[ind+1:]
        else:
            ind1=c.find('_')
            ind2=c.find('(')
            if ind1==-1 and ind2==-1:
                op.append(len(c))
                c=''
            else:
                if ind1==-1:
                    ind1=ind2
                if ind2==-1:
                    ind2=ind1
                op.append(min(ind1,ind2))
                c=c[min(ind1,ind2):]
    if op:
        print(max(op),end=' ')
    else:
        print(0,end=' ')
    for i in ip:
        x=i.split('_')
        x=list(filter(None,x))
        nip+=len(x)
    print(nip)