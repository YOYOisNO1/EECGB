def program2251():
    i = int(input())
    scores = list(map(int, input().split()))
    
    agg = {}
    for s in scores:
        if s == 0:
            continue
        agg[s] = agg.get(s, 0) + 1
    
    print(len(agg))