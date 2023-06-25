def program6193():
    r1,c1,r2,c2 = input().split()
    
    r1,c1,r2,c2 = int(r1), int(c1), int(r2), int(c2)
    lt=[]
    if r1==r2 or c1==c2:
        lt.append(1)
    else:
        lt.append(2)
    if (r1+r2+c1+c2)%2==0:
        if abs(r2-r1) == abs(c2-c1):
            lt.append(1)
        else:
            lt.append(2)
    else:
        lt.append(0)
    
    lt.append(max(abs(r2-r1), abs(c2-c1)))
        
    print(*lt)