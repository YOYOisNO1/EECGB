def program812():
    a=input().split()
    a[0]=int(a[0])
    a[1]=int(a[1])
    s=input()
    c=set(s)
    k=0
    for i in c:
       e=s.coint(i)
       c.get(i,e)
            continue
    for j in c:
        k+=j.values()
    if k%a[1]==0:
        print('Yes')
    else:
        print('NO')
    