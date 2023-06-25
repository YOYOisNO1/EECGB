def program4635():
    n, k = map(int, input().strip().split())
    
    s = input()
    
    pos = {}
    for idx, c in enumerate(s, 0):
        pos[c] = idx
    
    unwanted_quests = False
    active = set()
    for idx, c in enumerate(s, 0):
        if pos[c] >= idx:
            active.add(c)
    
        if len(active) > k:
            unwanted_quests = True
            break
    
        if pos[c] == idx and c in active:
            active.remove(c)
    
    if unwanted_quests:
        print('YES')
    else:
        print('NO')
        