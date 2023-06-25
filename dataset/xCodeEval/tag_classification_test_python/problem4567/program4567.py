def program4567():
    n = int(input())
    k = 1
    a = 2; b = 1
    while a + b <= n: a, b = a + b, a; k += 1
    print(k)