def program1157():
    a, b, c = [int(x) for x in input().split()]
    print min(a+b+c, 2*(a+b), 2*(a+c), 2*(b+c))