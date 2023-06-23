def program2593():
    L2=[]
    L=[]
    for i in range(4):
        L=[]
        ch=input()
        L.extend(ch)
        L2.append(L)   
    test=False    
    for i in range(3):
        for j in range(3):
            L1=[]
            L1.append(L2[i][j])
            L1.append(L2[i+1][j])
            L1.append(L2[i][j+1])
            L1.append(L2[i+1][j+1])
            if L1.count('.')>=3 or L1.count('#')>=3 4 
                test=True
                break
        if test:
            break
    if test:
        print('YES')
    else:
        print('NO')