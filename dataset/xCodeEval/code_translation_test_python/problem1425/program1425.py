def program1425():
    n = int(input())
    cnt = 0
    m = 9999999999999999
    piles = input().strip().split()
    for pile in piles:
        a = int(pile)
        if a < m:
            m = a
            cnt = 1
        elif a == m:
            cnt += 1
    if cnt <= n / 2:
        print("Alice")
    else:
        print("Bob")