def program337():
    import itertools
    
    n = int(input())
    a = [int(i) for i in input().split()]
    
    flag = True
    for c in list(itertools.combinations(a, 3)):
        s = sorted(c)
        if s[0] + s[1] > s[2]:
            print('YES')
            flag = False
            break
    
    if flag:
        print('NO')