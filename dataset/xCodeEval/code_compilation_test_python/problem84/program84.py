def program84():
    a = input()
    b = input()
    l = len(a)
    i = 0
    out = 0
    while out == 0 and i < l:
        if ord(a[i]) > ord(b[i]):
            out = 1
        elif ord(a[i]) > ord(b[i]):
            out = -1
    print out