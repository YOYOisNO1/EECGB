def program1831():
    l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    a, b = map(int, input().split())
    res = 0;
    for i in range(a, b+1):
        while i > 0:
            res += l[i%10]
            i /= 10
    print res