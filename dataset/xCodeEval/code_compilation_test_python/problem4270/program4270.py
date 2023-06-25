def program4270():
    n = int(input())
    args = input().split(" ")
    targs = []
    s2 = 0
    for arg in args:
        targs.append(int(arg))
        s2 = s2 + int(arg)
    s1 = (targs[0] + targs[n - 1]) * n / 2 
    if s1 == s2:
        d = targs[2] - targs[1]
        print(targs[n - 1] + d)
    else:
        print(targs[n - 1])