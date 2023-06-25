def program2234():
    n = int(input())
    pedacos = list(map(int, input().split()))
    j = 0
    k = 1
    ans = 1
    veri = True
    countOne = 0
    while j < len(pedacos):
        e = pedacos[j]
        if e == 1:
            countOne += 1
            if k != 0 and not veri:
                ans *= (k + 1)
            veri = False
            k = 0
        elif e == 0 and not veri:
            k += 1
        j += 1
    if countOne == 0:
        print(0)
    else:
        print(ans)