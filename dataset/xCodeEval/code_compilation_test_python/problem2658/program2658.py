    #debug = True
    
    import sys
    
    d = [-1, 1]
    
def out():
        FIN.close()
        FOUT.close()
        sys.exit()
    
    
    
    if debug:
        FIN = open('input.txt', 'r')
        FOUT = open('output.txt', 'w')
    else:
        FIN = sys.stdin
        FOUT = sys.stdout
        
    s = FIN.readline()
    if s[-1] == '\n':
        s = s[:-1]
    n = int(FIN.readline())
    f = [[[0 if (t == 1) and (j == 0) and (i == 0) else None for t in range(2)] for j in range(n + 1)] for i in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(n + 1):
            if s[i - 1] == 'F':
                for k in range(0, j + 1, 2):
                    for t in range(2):
                        if f[i - 1][j - k][t] is not None:
                            ff = f[i - 1][j - k][t] + d[t]
                            if f[i][j][t] is None or abs(ff) > abs(f[i][j][t]):
                                f[i][j][t] = ff
                for k in range(1, j + 1, 2):
                    for t in range(2):
                        ff = f[i - 1][j - k][t ^ 1]
                        if (ff is not None) and (f[i][j][t] is None or abs(ff) > abs(f[i][j][t])):
                            f[i][j][t] = ff
            else:
                for k in range(0, j + 1, 2):
                    for t in range(2):
                        ff = f[i - 1][j - k][t ^ 1]
                        if (ff is not None) and (f[i][j][t] is None or abs(ff) > abs(f[i][j][t])):
                            f[i][j][t] = ff
                for k in range(1, j + 1, 2):
                    for t in range(2):
                        if f[i - 1][j - k][t] is not None:
                            ff = f[i - 1][j - k][t] + d[t]
                            if f[i][j][t] is None or abs(ff) > abs(f[i][j][t]):
                                f[i][j][t] = ff
    if f[len(s)][n][0] is None:
        f[len(s)][n][0] = 0
    if f[len(s)][n][1] is None:
        f[len(s)][n][1] = 0  
    ans = max(abs(f[len(s)][n][0]), abs(f[len(s)][n][1]))
    FOUT.write(str(ans))
    out()
    