def program3183():
    x1=input().split()
    l1=[]
    for i in x1:
        i=int(i)
        l1.append(i)
    sum1=100000000000
    l2=l1.copy()
    for i in l2:
        c=0
        l1=l2.copy()
        z=l1.count(i)
        if z>1:
            if z>3:
                z=3
            while c<z:
                l1.remove(i)
                c+=1
        y=sum(l1)
        if sum1>y:
            sum1=y
    print(sum1)