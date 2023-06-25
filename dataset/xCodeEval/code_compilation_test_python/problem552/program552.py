def program552():
    f = open("input.txt")
    a = 10000
    b = -10000
    checker = 0
    for i in str(f).split()[:len(str(f)) - 3]:
        if checker % 2 == 0:
            if a > int(i):
                a = int(i)
        else:
            if b < int(i):
                b = int(i)
        checker += 1
    print(a + b)