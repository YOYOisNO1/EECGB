def program2936():
    k=[]
    for i in range(1,4):
        n=input()
        delimiter=' '
        n=n.split(delimiter)
        for h in n:
            k.append(h)
    l=[]
    for h in k:
        l.append(int(h))
        
        
    c=1
    delimiter=' '
    
    x1=l[0]+l[2]-l[4]
    y1=l[1]+l[3]-l[5]
    l1=[x1,y1]
    l1=str(l1)
    s1=delimiter.join(l1)
    x2=l[0]+l[4]-l[2]
    y2=l[1]+l[5]-l[3]
    l2=[x2,y2]
    l2=str(l2)
    s2=delimiter.join(l2)
    x3=l[2]+l[4]-l[0]
    y3=l[3]+l[5]-l[1]
    l3=[x3,y3]
    l3=str(l3)
    s3=delimiter.join(l3)
    
    if s1!=s2:
        c+=1
        if l2!=l3:
            c+=1
            print(c)
            print(('{0}) {1}'.format(x1,y1))
            print(('{0}) {1}'.format(x2,y2))
            print(('{0}) {1}'.format(x3,y3))
    
        else:
            print(c)
            print(('{0}) {1}'.format(x1,y1))
            print(('{0}) {1}'.format(x2,y2))
    
    else:
        if s2!=s3:
            c+=1
            print(c)
            print(('{0}) {1}'.format(x1,y1))
            print(('{0}) {1}'.format(x3,y3))
            
        else:
            print(c)
            print(('{0}) {1}'.format(x1,y1))
        
        
        
            
            
    
            
            