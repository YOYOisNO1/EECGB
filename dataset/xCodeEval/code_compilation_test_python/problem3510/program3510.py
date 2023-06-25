def program3510():
    line = input()
    previous = ''
    res = 0
    consecutive = 0
    for c in line:
        if consecutive == 5:
            consecutive = 0
            res = res + 1
        if c == previous:
            consecutive = consecutive + 1
        else:
            if consecutive != 0:
                res = res + 1
            consecutive = 1
        prev = c
    if consecutive != 0:
        res = res + 1
    print res