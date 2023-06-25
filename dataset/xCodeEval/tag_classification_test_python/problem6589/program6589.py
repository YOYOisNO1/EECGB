def program6589():
    ceil1 = lambda a, b: (a + b - 1) // b
    x = int(input())
    if x == 3:
        print(5)
    else:
        for i in range(1, 16, 2):
            ma = ceil1(i ** 2, 2)
            if ma >= x:
                print(i)
                exit()