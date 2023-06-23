def program2918():
    s = list(input())
    n = len(s)
    res = []
    i = 0 
    while(n > 0):
        if s[0] == '.':
            res.append('0')
            s.pop(0)
            n -= 1
        elif s[1] == '.':
            res.append('1')
            s.pop(0)
            s.pop(0)
            n -= 2
        else':
            res.append('2')
            s.pop(0)
            s.pop(0)
            n -= 2
    print("".join(res))