def pr(u):
        for i in range(6):
            s = ''
            for j in range(8):
                s += u[i][j]
            print(s)
    
    p = []
    for i in range(6):
        s = input()
        p.append(list(s))
    
    for i in range(6):
        if p[i][3] == '.':
            p[i][3] = 'P'
            pr(p)
            break
        if p[i][4] == '.':
            p[i][4] = 'P'
            pr(p)
            break
        if p[i][0] == '.':
            p[i][0] = 'P'
            pr(p)
            break
        if p[i][1] == '.':
            p[i][1] = 'P'
            pr(p)
            break
        if p[i][6] == '.':
            p[i][6] = 'P'
            pr(p)
            break
        if p[i][7] == '.':
            p[i][7] = 'P'
            pr(p)
            break
    
        
    