def program423():
    n, k = map(int, input().split())
    sito = [True for _ in range(1050)]
    wynik = 0
    for x in range(2, n + 50):
        for y in range(x*2, n + 50, x):
            sito[y] = False
    pierwsze = []
    for x in range(1, n):
        if sito[x]:
            pierwsze.append(x)
    for x in range(len(pierwsze) - 1):
        if sito[pierwsze[x] + pierwsze[x+1] + 1] and pierwsze[x] + pierwsze[x+1] + 1 <= n:
            wynik += 1
    if wynik >= k:
        print("YES")
    else:
        print("NO")