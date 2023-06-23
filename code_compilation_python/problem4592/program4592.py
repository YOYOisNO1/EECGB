def get(a):
        global m
        R = -1
        G = -1
        mi = -1
        for i in range(m):
            if a[i] == '-':
                mi = i
            elif a[i] == "R":
                R = i
            else:
                G = i
        return G, R, mi
    
    
    n, m, k = map(int, input().split())
    draw = [0, 0]
    t = []
    for i in range(n):
        G, R, mi = get(input())
        if G == -1:
            if R != -1 and mi != -1:
                draw[1] = 1
        elif R == -1:
            if mi != -1:
                draw[0] = 1
        else:
            t.append(abs(G - R) - 1)
    if not t:
        if not draw[0]:
            print("Second")
        elif not draw[1]:
            print("First")
        else:
            print("Draw")
        exit()
    winner = 1
    for bit in range(7):
        tmp = 0
        for i in range(len(t)):
            tmp += t[i] & 1
            t[i] >>= 1
        if tmp % (k + 1) != 0:
            winner = 0
            break
    draw[winner] = 0
    if draw[1 - winner]:
        print("Draw")
    else:
        print("First" if winner == 0 else "Second")