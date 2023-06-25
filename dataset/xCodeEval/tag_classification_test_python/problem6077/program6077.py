def program6077():
    from sys import stderr
    
    a = [tuple(map(int, input().split())) for i in range(8)]
    
    x = sorted(list(set([i[0] for i in a])))
    y = sorted(list(set([i[1] for i in a])))
    
    print(a, file = stderr)
    print(x, y, file = stderr)
    
    if len(x) != 3 or len(y) != 3:
        print('ugly')
    else:
        ans = 'respectable'
        for i in x:
            for j in y:
                if (i != x[1] or j != y[1]) and (i, j) not in a:
                    ans = 'ugly'
        if (x[1], y[1]) in a:
            ans = 'ugly'
        print(ans)