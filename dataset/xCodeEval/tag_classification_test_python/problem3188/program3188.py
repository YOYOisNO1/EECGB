def program3188():
    prev = ''
    h = 0
    n = 0
    for ch in input():
        if ch != prev or h == 5:
            h = 1
            n += 1
        else:
            h += 1
        prev = ch
    print(n)