def program544():
    l=[]
    for i in range(int(input())):
        l.append(int(input()))
    p={1,2}
    s=3
    for x in l:
        if x not in p:
            print('NO')
            break
        t={x,s}
        s=list(p-{x})
        s=s[0]
        p=t
    else:
        print('YES')