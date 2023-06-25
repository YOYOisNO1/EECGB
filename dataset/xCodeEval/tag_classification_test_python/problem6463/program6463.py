def program6463():
    n = int(input())
    data = set(input().split())
    cards = []
    lets = 'RGBYW'
    ans = 10
    for i in data:
        p1 = lets.find(i[0])
        p2 = int(i[1]) - 1
        cards.append(2 ** p1 +  2 ** (p2 + 5))
    for i in range(1024):
        good = True
        for j in range(len(cards) - 1):
            for k in range(j + 1, len(cards)): 
                if (cards[j] & i) == (cards[k] & i):
                    good = False
        if good:
            ones = 0
            now = i
            while now != 0:
                ones += now % 2
                now //= 2
            ans = min(ans, ones)
    print(ans)