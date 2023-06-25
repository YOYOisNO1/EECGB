def program1099():
    a = int(input())
    b = int(input()
    c = a % b
    d = a
    while c != 0:
        d += c
        c = c % b
    print(d)