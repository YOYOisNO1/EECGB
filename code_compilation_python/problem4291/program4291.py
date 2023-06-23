def program4291():
    t = input()
    s = None
    for i in reversed(range(1, len(t))):
        if t[i] != t[0]:
            continue
        if (i < len(t) - i) and (t.startswith(t[i:])):
            s = t[i:]
    if s is not None:
        print('YES\n', s, sep ='')
    else:
        print('NO\n')