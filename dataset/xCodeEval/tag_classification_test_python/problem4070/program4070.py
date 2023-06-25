def program4070():
    a=input()
    a=a.replace('WUB','   ')
    a=a.lstrip()
    a=a.rstrip()
    flag=0
    b=""
    c=[]
    for i in range(len(a)):
        if a[i]!=" ":
            b+=a[i]
        else:
            c.append(b)
            b=""
        if i==len(a)-1:
            c.append(b)
    for i in range(len(c)):
        if c[i]!="":
            print(c[i],end=" ")