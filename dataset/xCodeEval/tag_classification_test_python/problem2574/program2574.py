def program2574():
    a, b = 0, 3
    for i in range(int(input()) - 1):
        a, b = b % 1000000007, (2 * b + 3 * a) % 1000000007
    print(a)