def program4324():
    a, b, c = map(int, (input() for i in range(3)))
    A = min(a, b//2, c//4)
    print(7*A)