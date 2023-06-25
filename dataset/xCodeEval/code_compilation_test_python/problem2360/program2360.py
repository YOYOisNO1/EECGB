def program2360():
    G = (1 + 5 ** .5) / 2
    w = set((int(k * G), int(k * G) + k) for k in range(999))
    n = input()
    a = sorted(map(int, input().split()))+[0,0]
    print 'BitAryo' if (((a[0], a[1]) in w) if 2==n else not(a[0]^a[1]^a[2])) else 'BitLGM'