def program3559():
    n, t = map(int, input().split())
    s = [c for c in input()]
    for _ in range(t):
        i = 0
        while i < n:
            if i < n-1 and s[i] == 'B' and s[i+1] == 'G':
                s[i] = 'G'
                s[i+1] = 'B'
                i += 2
            else:
                i += 1
    
    print(''.join(s))