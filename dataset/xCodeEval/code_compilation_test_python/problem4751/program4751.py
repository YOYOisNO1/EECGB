def program4751():
    a = input()
    b = input()
    
    tab = [[[None] * 220 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    par = [[[None] * 220 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    
    tab[0][0][0] = 0
    que = [(0, 0, 0)]
    index = 0
    while tab[len(a)][len(b)][0] is None:
        i,j,bal = que[index]
        if bal<218:
            #Add (
            ii=i
            jj=j
            if i<len(a) and a[i]=='(':
                ii=i+1
            if j<len(b) and b[j]=='(':
                jj=j+1
            if tab[ii][jj][bal+1] is None:
                tab[ii][jj][bal + 1] = tab[i][j][bal]+1
                par[ii][jj][bal + 1] = i,j,bal,'('
                que.append((ii,jj,bal+1))
        if bal>0:
            ii = i
            jj = j
            # Add )
            if i<len(a) and a[i] == ')':
                ii = i + 1
            if j<len(b) and b[j] == ')':
                jj = j + 1
            if tab[ii][jj][bal - 1] is None:
                tab[ii][jj][bal - 1] = tab[i][j][bal] + 1
                par[ii][jj][bal - 1] = i, j, bal, ')'
                que.append((ii, jj, bal - 1))
        index+=1
    
    i = len(a)
    j = len(b)
    bal = 0
    answer=[]
    while (i,j,bal) != (0,0,0):
        # print (i,j,bal)
        i,j,bal,symb = par[i][j][bal]
        answer.append(symb)
    print(''.join(reversed(answer)))