def program1781():
    n = input().split(' ')
    n1 = int(n[0])
    m = int(n[1])
    while True:
        for i in range(1, n1 + 1):
            if m > i:
                m -= i
            else:
                break
            if i == n1:
                i = 1
        if m < i:
            break
    print(m)