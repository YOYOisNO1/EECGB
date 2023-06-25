def program726():
    a, b = map(int, input().split())
    b_2, b_3, b_5 = 0, 0, 0
    a_2, a_3, a_5 = 0, 0, 0
    while b % 2 == 0:
        b_2 += 1
        b //= 2
    while b % 3 == 0:
        b_3 += 1
        b //= 3
    while b % 5 == 0:
        b_5 += 1
        b //= 5
    while a % 2 == 0:
        a_2 += 1
        a //= 2
    while a % 3 == 0:
        a_3 += 1
        a //= 3
    while a % 5 == 0:
        a_5 += 1
        a //= 5
    if a != b:
        print(-1)
    else:
        print(abs(a_2 - b_2) + abs(a_3 - b_3) + abs(a_5 - b_5))