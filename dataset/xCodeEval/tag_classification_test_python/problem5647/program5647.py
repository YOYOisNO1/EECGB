def fact(x):
        f = 1
        if x <= 1:
            return f
        else:
            for i in xrange(1, x + 1):
                f *= i
        return f
        
    a, b = map(int, input().split())
    if a > b:
        print(fact(b))
    else:
        print(fact(a))