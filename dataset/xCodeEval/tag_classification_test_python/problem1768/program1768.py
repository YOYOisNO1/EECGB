def program1768():
    l=list()
    for i in [0,1,2,3,4]:
        p = list(map(int, input().split()))
        l.append(p)
    
    x=0
    y=0
    for m in [0,1,2,3,4]:
        for n in [0,1,2,3,4]:
            if l[m][n]==1:
                x=m
                y=n
    c=0
    c=abs(x-2)+abs(y-2)+c
    print(c)
    
    
    