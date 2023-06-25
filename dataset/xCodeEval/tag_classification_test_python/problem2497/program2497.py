def program2497():
    A = input()
    a = int(A, 2)
    b = int(input(), 2)
    c = str(bin(a ^ b)[2:])
    while len(c) < len(A):
        c = '0' + c
    print(c)