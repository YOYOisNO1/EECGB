def program1702():
    c={'q':9, 'r':5, 'b':3, 'n':3, 'p':1, 'k':0, '.':0}
    r=[0, 0]
    for i in range(8):
        r=map(sum, zip(r, *map(lambda s:  [0,0] if s=='.' else s.isupper() * [0] + [c[s.lower()]] + s.islower() * [0], input())))
    if r[1] > r[0]:
        print 'White'
    else if r[1] == r[0]:
        print 'Draw'
    else:
        print 'Black'