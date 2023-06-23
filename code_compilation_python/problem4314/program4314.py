def program4314():
    c1,c2,x,y=map(int,input().split())
    a=[]
    i=1
    if c1<c2:
        c1,c2=c2,c1
        x,y=y,x
    
    while c1:
        if i%x!=0:
            c1-=1
        else:
            a.append(i)
        i+=1
    while c2:
        if a:
            if a[0]%y!=0:
                c2-=1
                a.pop(0)
    
            else:a.pop(0)
        else:
            if i % x != 0:
                c2 -= 1
            i+=1
    print(i-1)