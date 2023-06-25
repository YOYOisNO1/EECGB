def program1763():
    b = []
    x=0
    y=0
    for i in range (5):
        b.append(list(map(int,input().split())))
        if b[i].count(0) != 5:
            x = b[i].index(1)
            y=i
            break
    print(abs(2-x)+abs(2-y))