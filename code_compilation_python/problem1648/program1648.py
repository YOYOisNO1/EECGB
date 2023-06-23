def program1648():
    str = str(input())
    k = str.split(' ')
    a = k[0]
    b = k[1]
    as = a + b
    m = ""
    n = ""
    for i in a:
        m += i
        for j in b:
            n += j
            if as > m + n:
                as = m + n
        n = ""
    print(as)