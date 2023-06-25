def program6159():
    co=input()
    co=co.split()
    r1=int(co[0])
    c1=int(co[1])
    r2=int(co[2])
    c2=int(co[3])
    
    result=[0,0,0]
    
    if c1-c2!=0:
        result[0]+=1
    if r1-r2!=0:
        result[0]+=1
    
    if (c1+r1)%2==(c2+r2)%2:
        if abs(c1-c2)==abs(r1-r2):
            result[1]=1
        else:
            result[1]=2
    
    if abs(c1-c2)>abs(r1-r2):
        result[2]=abs(c1-c2)
    else:
        result[2]=abs(r1-r2)
    
    result[0]=str(result[0])
    result[1]=str(result[1])
    result[2]=str(result[2])
    
    print(" ".join(result))