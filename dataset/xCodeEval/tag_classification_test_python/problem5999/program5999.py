def program5999():
    import itertools
    
    
    a = list(map(int, input().split()))
    
    s = sum(a)
    
    for i in itertools.permutations(a, 3):
        if sum(i) * 2 == s:
            print('YES')
            exit()
    print('NO')