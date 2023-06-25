def program1735():
    import math
    n = int(input())
    if n <= 2:
        print(n+1)
        exit()
    sqr = math.sqrt(n)
    if sqr == int(sqr):
        print(int(sqr+sqr))
        exit()
    else:
        if n % 2 == 1:
            n += 1
        test = math.sqrt(n+1)
        if test == int(test):
            print(test+test)
            exit()
        sqr = math.ceil(math.sqrt(n))
        for i in range(sqr, 1, -1):
            if n % i == 0:
                opt = i + n//i
        n += 1
        sqr = math.ceil(math.sqrt(n))
        for i in range(sqr, 1, -1):
            if n % i == 0:
                opt2 = i + n//i
        print(min(opt, opt2))