def program3216():
    from sys import stdin
    rr = lambda: stdin.readline().strip()
    rrm = lambda: map(int, rr().split())
    
    S = rr()
    print(S[0].upper()) + S[1:]