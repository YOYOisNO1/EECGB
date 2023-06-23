def program3273():
    p1,p2,valid=1,2,True
    for i in range(int(input()):
        a=int(input())
        if valid:
            continue
        if a!=p1 and a!=p2:
            valid=False
        s=6-p1-p2
        if a==p1:
            p2=s
        else:
            p1=s
    if valid:
        print('YES')
    else:
        print('NO')