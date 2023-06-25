def program4752():
    a = input()
    b = input()
    
    m = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    # bil = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    dir = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    a = a[::-1]
    b = b[::-1]
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                # if a[i]=='(':
                #     bil[i+1][j+1]=m[i][j]+1
            elif m[i][j + 1] == m[i + 1][j]:
                m[i + 1][j + 1] = m[i][j + 1]
                if a[i] == '(':
                    dir[i + 1][j + 1] = 1
                else:
                    dir[i + 1][j + 1] = 2
            else:
                m[i + 1][j + 1], dir[i + 1][j + 1] = max((m[i][j + 1], 1), (m[i + 1][j], 2))
    
    # print('\n'.join(map(str, m)))
    # print('\n'.join(map(str, dir)))
    
    ii = len(a)
    jj = len(b)
    
    answer = []
    while ii and jj:
        if dir[ii][jj] == 0:
            answer.append(a[ii - 1])
            ii -= 1
            jj -= 1
        elif dir[ii][jj] == 1:
            answer.append(a[ii - 1])
            ii -= 1
        elif dir[ii][jj] == 2:
            answer.append(b[jj - 1])
            jj -= 1
        # print (ii, jj)
    
    while ii>0:
        answer.append(a[ii-1])
        ii-=1
    while jj>0:
        answer.append(b[jj-1])
        jj-=1
    
    
    level = 0
    mlev=0
    for aa in answer:
        if aa=='(':
            level+=1
        else:
            level-=1
        mlev = min(level,mlev)
    
    pref = ''
    suf = ''
    
    if mlev<0:
        pref = -mlev * '('
    level -=mlev
    if level>0:
        suf = level*')'
    
    answer = pref + ''.join(answer) + suf
    
    print(answer)
    
    """
    ( ( )) (  ()
    (   ))  ) ()
    
    (())()()
    """
    
    """
    ()
    (())
    """