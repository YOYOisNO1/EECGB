def program373():
    n, a = map(int,input().split())
    l = list(map(int,input().split()))
    city = (1 if l[a-1] == 1 else 0)
    distance = 1
    
    a-=1
    while a-distance>=0 or a+distance<n:
        c = 0
        if a-distance >= 0:
            if l[a-distance]==1:
                c+=1
        else:
            c+=1
        if a+distance < n:
            if l[a+distance]==1:
                c+=1
        else:
            c+=1
        if c == 2 and a-distance>=0 and a+distance<n:
            city+=2
        elif c == 2:
            city+=1
        
        
        distance+=1
    print(city)
    '''
    20 17
    1 1 0 1 1 1 1 0 1 0 1 1 1 0 1 1 0 0 0 0
    '''