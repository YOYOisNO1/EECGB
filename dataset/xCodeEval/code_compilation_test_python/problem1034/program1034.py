def program1034():
    import sys
    for line in sys.stdin:
        line = line.rstrip()
        n = int(line)
        a = 1
        while(True):
            if n == 1: break
            n = floor(n / 2.0)
            a += 1
        print(a)