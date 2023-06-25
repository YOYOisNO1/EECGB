def program1576():
    n = int(input())
    a = map(int,input().split())
    if n is 0:
        print(('0'))
        exit()
    c = 0
    for i, v in enumerate(reversed(sorted(a))):
        c += v
        if c >= n:
            print((i) + 1)
            exit()
    print((-1))