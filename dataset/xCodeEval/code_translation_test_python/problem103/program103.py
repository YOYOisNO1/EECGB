def main():
        ls = []
        for i in range(11):
            l = list(filter(lambda c: c != ' ', input()))
            if l:
                ls.append(l)
    
        r, c = list(map(lambda c: int(c) - 1, input().split(' ')))
    
        flag = False
        cr, cc = r % 3, c % 3
        for i in range(cr * 3, cr * 3 + 3):
            for j in range(cc * 3, cc * 3 + 3):
                if ls[i][j] not in ['x', 'o']:
                    ls[i][j] = '!'
                    flag = True
        
        if not flag:
            for i in range(9):
                for j in range(9):
                    if ls[i][j] not in ['x', 'o']:
                        ls[i][j] = '!'
    
        for i in range(3):
            for j in range(3):
                l = ls[i * 3 + j]
                print(' '.join(map(lambda xx: ''.join(xx), [l[0:3], l[3:6], l[6:9]])))
            print('')
    
    main()