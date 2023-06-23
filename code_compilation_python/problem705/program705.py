def program705():
    from math import ceil
    n = int(input())
    i = 0
    while True:
        if n % (3 ** i) != 0:
            print(ceil(n / (3 ** i)))
            exit()
        i += 1