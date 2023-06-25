def program347():
    n = int(input())
    if n == 1:
        print(3)
        exit()
    a = (n-1)//3+1
    b = n%3
    if b == 0:
        print(4*a+3)
    elif b == 1:
        print(4*a)
    else:
        print(4*a+1)