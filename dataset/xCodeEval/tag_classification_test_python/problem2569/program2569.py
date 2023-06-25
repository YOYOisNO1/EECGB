def program2569():
    n,a,x,b,y = list(map(int,input().split()))
    
    t = 0
    find = False
    
    A = False
    B = False
    
    while(not A or not B):
    
        if a == b and A == False and B == False:
            find = True
            break
    
        if a != x:
            a += 1
    
            if a > n:
                a = 1
        else:
            A = True
    
        if b != y:
            b -= 1
    
            if b == 0:
                b = n
        else:
            B = True
    
        # print(a,b)
    
    
        t+=1
    # print(visited)
    print('YES' if find else 'NO')