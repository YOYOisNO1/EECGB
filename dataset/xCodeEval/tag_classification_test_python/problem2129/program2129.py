def tree(k, n):
        tab = [[0 for _ in xrange(k + 1)] for _ in xrange(n + 1)]
        for i in xrange(0, k + 1):
            tab[0][i] = 1
        for i in xrange(1, n + 1):
            tab[i][0] = 0
            for j in xrange(1, k + 1):
                if (i < j):
                    tab[i][j] = tab[i][j - 1]
                else:
                    tab[i][j] = (tab[i][j - 1] + tab[i - j][k]) % modulo
        return tab[n][k]
        
    n, k, d = map(int, input().split())
    modulo = 1000000007
    
    if (d < 2):
      print(tree(k,) n)
    else:
      print((tree(k,) n) - tree(d - 1, n)) % modulo