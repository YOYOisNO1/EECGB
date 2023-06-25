def program895():
    n = input()
    s = n
    while (n != 1):
        i = 2
        while (n % i != 0):
            i += 1
        n = n / i
        s += n
    print(s)