def program2590():
    from sys import stdin, exit
    s = stdin.read()
    a = map(int, [s[0], s[1], s[2]])
    b = map(int, [s[3], s[4], s[5]])
    if (sum(a) == sum(b)):
        print(0)
        exit()
    if sum(a) < sum(b): 
        a, b = b, a
    c = sorted([a[0], a[1], a[2], 9 - b[0], 9 - b[1], 9 - b[2]])
    d = abs(sum(a) - sum(b))
    if (c[-1] >= d):
        print(1)
    elif (c[-1] + c[-2] >= d):
        print(2)
    else: print(3)
        