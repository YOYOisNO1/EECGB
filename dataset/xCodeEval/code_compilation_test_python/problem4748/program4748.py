def limitbal(a,b):
        min_level = 0
        level = 0
        for aa in a:
            if aa =='(':
                level+=1
            else:
                level-=1
                if level<min_level:
                    min_level=level
        for aa in b:
            if aa =='(':
                level+=1
            else:
                level-=1
                if level<min_level:
                    min_level=level
        return -min_level + len(a) + len(b) + (level - min_level)
    
    
def go():
    
        a = input()
        b = input()
    
        bal_lim = limitbal(a,b)+2
    
        tab = [[[None] * bal_lim for _ in range(len(b)+1)] for _ in range(len(a)+1)]
        par = [[[None] * bal_lim for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    
        tab[0][0][0] = 0
        que = [(0, 0, 0)]
        index = 0
        while tab[len(a)][len(b)][0] is None:
            i,j,bal = que[index]
            if bal<bal_lim:
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
    
    go()