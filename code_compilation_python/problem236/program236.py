def program236():
    n, s = input(), input()
    while len(s) > 1: s = s.replace('BB', 'B').replace('RR', 'R').replace('GG', 'G')
    print(n-len(s))