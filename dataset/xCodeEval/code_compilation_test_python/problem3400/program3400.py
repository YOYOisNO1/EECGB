def program3400():
    n = int(input())
    c = 1
    for i in range(1, 20):
        tmp = (2**i - 1)*(2**(i-1))
        if (n % tmp) == 0:
        c = tmp
    print(c)