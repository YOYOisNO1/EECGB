def program4235():
    
    
    
    t=[]
    
    u=0
    for i in range(8):
    
        a= list(input())
        if a.count('B')==a.count('W'):
            for k in range(7):
                if a[k]!=a[k+1]:
                    pass
                else:
                    u+=1
        else:
            u+=1
        t.append(a)
    
    
    if u>0:
        print('NO')
    else:
        print('YES')