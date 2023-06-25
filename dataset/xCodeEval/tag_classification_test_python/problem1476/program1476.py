def program1476():
    d = {0: 6, 1: 8, 2: 4, 3: 2}
    n = int(input())
    if n: print(d[n % 4])
    else: print(1)