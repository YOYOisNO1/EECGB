def program1896():
    from itertools import combinations
    n = int(input())
    ls = [x for x in range(1, min(45, n+1))]
    try:
        for i in range(n, 0, -1):
            cs = list(combinations(ls, min(45, i)))
            for c in cs:
                if sum(c) == n:
                    raise
    except:
        print(len(c), '\n' + ' '.join(map(str, c)))