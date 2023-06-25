def program3824():
    import itertools
    
    n = int(input())
    a = []
    for i in range(n):
        lst = list(map(int, input().split()))
        a.append(lst)
    i = 0
    while i < 10 ** n - 1:
        ch = i + 1
        c = []
        while ch > 0:
            z = ch % 10
            kek = []
            for j in range(n):
                if z in a[j]:
                    kek.append(j)
            c.append(kek)
            ch //= 10
    
        if len(c) == 1:
            if len(c[0]) > 0:
                i += 1
            else:
                break
            continue
        
        if len(c) == 2:
            ok = 0
            for i1 in c[0]:
                for j1 in c[1]:
                    if i1 != j1:
                        ok = 1
            if ok:
                i += 1
            else:
                break
        if len(c) == 3:
            ok = 0
            for i1 in c[0]:
                for j1 in c[1]:
                    for k1 in c[2]:
                        if i1 != j1 and j1 != k1:
                            print(i1, j1, k1)
                            i += 1
                            ok = 1
                            break
            if not ok:
                break
        
    print(i)