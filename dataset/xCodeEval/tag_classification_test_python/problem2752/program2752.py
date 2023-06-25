def program2752():
    import math
    n, m, t = map(int, input().split())
    pos = 0
    
    for i in xrange(1, m + 1):
        for j in xrange(4, n + 1):
            if i + j == t:
                a =  math.factorial(n)/(math.factorial(n - j) * math.factorial(j))
                a *= math.factorial(m)/(math.factorial(m - i) * math.factorial(i))
                pos += a
    print(pos)