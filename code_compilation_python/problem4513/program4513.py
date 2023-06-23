def program4513():
    print(min(*[(x for x in range(103) if a.count(x) == 0) for a in [[list(map(int, input().split())) for _ in range(2)][1]]]))