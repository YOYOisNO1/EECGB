def program2531():
    hand = input().split()
    s_hand = [[] for i in range(3)] # m, p, s
    shuntsu = 100
    for i in hand:
        s_hand['mps'.index(i[1])].append(int(i[0]))
    for i in s_hand:
        if not i:
            continue
        if len(i) == 1:
            shuntsu = min(shuntsu, 2)
        elif len(i) == 2:
            shuntsu = min(shuntsu, 1 if abs(i[0] - i[1]) in (1, 2) else 100)
        else:
            s_i = sorted(i)
            if s_i[0] + 1 == s_i[1] and s_i[1] + 1 == s_i[2]:
                shuntsu = 0
            else:
                shuntsu = min(shuntsu, min(1 if abs(i[0] - i[1]) in (1, 2) else 100, 1 if abs(i[1] - i[2]) in (1, 2) else 100, 1 if abs(i[0] - i[2]) in (1, 2) else 100))
    t = len(set(hand))
    koutsu = 0 if t == 1 else 1 if t == 2 else 2
    
    print(min(shuntsu, koutsu))