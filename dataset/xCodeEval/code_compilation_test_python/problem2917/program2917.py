def program2917():
    s = input()
    r = []
    i = 0
    l = len(s)
    while i < l:
        if s[i] == '-':
            if s[i+1] == '-':
                r.append(2)
            else:
                r.append(1)
            i += 2
        else:
            r.append(0)
            i += 1
    return ''.join(map(str, r))