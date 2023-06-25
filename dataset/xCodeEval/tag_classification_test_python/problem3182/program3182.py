def program3182():
    from collections import Counter
    
    t = list(map(int, input().split()))
    cnt = Counter(t)
    res = 0
    for el in cnt:
        if cnt[el] >= 3:
            res = max(res, 3 * el)
        elif cnt[el] == 2:
            res = max(res, 2 * el)
    print(sum(t) - res)