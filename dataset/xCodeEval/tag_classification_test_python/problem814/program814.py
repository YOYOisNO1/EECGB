def program814():
    m = [0] * 10
    for i in xrange(1, 10):
        m[i] = m[i-1] + i*9*(10**(i-1))
    n = input()
    c = len(n)
    print(m[c-1]) + (int(n) - (10**(c-1) -1))*c