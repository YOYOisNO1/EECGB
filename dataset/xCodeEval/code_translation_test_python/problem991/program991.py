def program991():
    n = input()
    domino = []
    for i in range(n):
        domino.append(map(int, input().split()))
    upper_sum = 0
    lower_sum = 0
    for i in range(n):
        card = domino[i]
        upper_sum += card[0]
        lower_sum += card[1]
    if (upper_sum + lower_sum) % 2 != 0:
        print(-1)
    elif upper_sum % 2 == 0:
        print(0)
    else:
        flag = True
        for i in range(n):
            if sum(domino[i]) % 2 != 0:
                flag = False
                break
        print(-1) if flag else 1