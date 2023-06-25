def program6132():
    r1,c1,r2,c2=map(int,input().split())
    a=[]
    if r1==r2 or c1==c2:
        a.append(1)
    else:
        a.append(2)
    if abs(r1-r2)==abs(c1-c2):
        a.append(1)
    elif (r1+c1)%2==0 and (r2+c2)%2!=0 or (r1+c1)%2!=0 and (r2+c2)%2==0:
        a.append(0)
    else:
        a.append(2)    
    if abs(r1-r2)==abs(c1-c2):
        a.append(abs(r1-r2))
    else:
        a.append(max(abs(r1-r2),abs(c1-c2)))
    print(*a)                      