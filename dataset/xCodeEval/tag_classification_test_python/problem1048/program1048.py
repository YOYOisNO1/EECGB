def program1048():
    from itertools import permutations
    
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    awin = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    
    amin = n
    pairs = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 0)]
    for seq in permutations(pairs):
        aa = a.copy()
        bb = b.copy()
        b_win = 0
        for pair in seq:
            ai = pair[1]
            bi = pair[0]
            delta = min(aa[ai], bb[bi])
            aa[ai] -= delta
            bb[bi] -= delta
            b_win += delta
        amin = min(amin, n - b_win)
    
    print(amin, awin)
    