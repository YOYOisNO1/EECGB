def program141():
    word = input()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wordidx = [alpha.index(i) for i in word]
    fibidx = [wordidx[0], wordidx[1]]
    while len(fibidx) != len(wordidx):
        fibidx.append((fibidx[-1]+fibidx[-2])%26)
    print("YES") if fibidx == wordidx else print("NO")