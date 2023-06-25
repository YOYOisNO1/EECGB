def program86():
    n = int(input())
    mod4 = n % 4
    if mod4 == 1:
        print(8)
    elif mod4 == 2:
        print(4)
    elif mod4 == 3:
        print(2)
    elif n == 0:
        print(1)
    else:
        print(6)