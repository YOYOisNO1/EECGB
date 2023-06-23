def program2130():
    n=input("")
    cnt=[0,0,0,0,0,0,0,0,0,0]
    
    for i in range(int(4)):
        x=input("")
        for c in x:
            cnt[int(c)]+=1
    
    flag=False
    
    for i in range(1,10):
        if cnt[i]>n*2:
            flag=False
            break
        else:
            flag=True
    
    if flag:
        print 'NO'
    else:
        print 'YES'
    
        