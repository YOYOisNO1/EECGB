def find(r, c, s1, s2):
        combo = 0
        while a[r][c] == 'X':
            r += s1
            c += s2
            combo += 1
        return combo
    
    a = ['@@@@@@@@@@@@']
    marks = []
    dots = []
    ans = 1
    for i in range(10):
        a.append('@' + input() + '@')
    a.append('@@@@@@@@@@@@')
    
    for i in range(1, 11):
        for j in range(1, 11):
            if a[i][j] == '.':
                res1 = find(i, j-1, 0, -1) + find(i, j+1, 0, 1)
                res2 = find(i+1, j, 1, 0) + find(i-1, j, -1, 0)
                res3 = find(i+1, j+1, 1, 1) + find(i-1, j-1, -1, -1)
                res4 = find(i+1, j-1, 1, -1) + find(i-1, j+1, -1, 1)
                if res1 > 3 or res2 > 3 or res3 > 3 or res4 > 3:
                    ans = 0
                 
    print('YNEOS'[ans::2])