def program1258():
    n = input()
    txt = str(input())
    wyn = 0
    wyn2 = 1
    lit = ''
    for x in range(0, n-1, +1):
        wyn2 = 1
        for y in range(1, n-1, +1):
            if txt[y] == txt[x] and txt[y+1] == txt[x+1]:
                wyn2 += 1
        if wyn2 > wyn:
            wyn = wyn2
            lit = txt[x]+txt[x+1]
    print(lit)