def limitbal(a, b):
        min_level = 0
        level = 0
        for aa in a:
            if aa == '(':
                level += 1
            else:
                level -= 1
                if level < min_level:
                    min_level = level
        for aa in b:
            if aa == '(':
                level += 1
            else:
                level -= 1
                if level < min_level:
                    min_level = level
        return -min_level + len(a) + len(b) + (level - min_level)
    
    
def go():
        a = input()
        b = input()
        lena = len(a)
        lenb = len(b)
        a+='X'
        b+='X'
    
        bal_lim = limitbal(a, b) + 2
    
        tab = [[[None] * bal_lim for _ in range(lenb + 1)] for _ in range(lena+1)]
        par = [[[None] * bal_lim for _ in range(lenb + 1)] for _ in range(lena+1)]
    
        tab[0][0][0] = 0
        que = [(0, 0, 0)]
        index = 0
        while tab[lena][lenb][0] is None:
            i, j, bal = que[index]
    
            ai = a[i]
            bj = b[j]
    
            if bal < bal_lim and (bal==0 or not (ai==bj==')')):
                # Add (
                ii = i
                jj = j
                if ai == '(':
                    ii = i + 1
                if bj == '(':
                    jj = j + 1
                if tab[ii][jj][bal + 1] is None:
                    tab[ii][jj][bal + 1] = tab[i][j][bal] + 1
                    par[ii][jj][bal + 1] = i, j, bal, '('
                    que.append((ii, jj, bal + 1))
            if bal > 0 and not (ai==bj=='('):
                ii = i
                jj = j
                # Add )
                if ai == ')':
                    ii = i + 1
                if bj == ')':
                    jj = j + 1
                if tab[ii][jj][bal - 1] is None:
                    tab[ii][jj][bal - 1] = tab[i][j][bal] + 1
                    par[ii][jj][bal - 1] = i, j, bal, ')'
                    que.append((ii, jj, bal - 1))
            index += 1
    
        i = lena
        j = lenb
        bal = 0
        answer = []
        while (i, j, bal) != (0, 0, 0):
            # print (i,j,bal)
            i, j, bal, symb = par[i][j][bal]
            answer.append(symb)
        print(''.join(reversed(answer)))
    
    
    go()