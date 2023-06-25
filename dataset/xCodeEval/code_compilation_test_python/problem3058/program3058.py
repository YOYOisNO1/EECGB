def program3058():
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = 0
    turn = 0
    for i in range(n):
        turn += a[i]
        if turn >= m :
            b += 1
            turn = a[i]
    if a[-1] + a[-2] > m :
        b += 1
    print(b)