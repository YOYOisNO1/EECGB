def program3102():
    # Design_by_JOKER
    import math
    import cmath
    
    s = list(input())
    n = len(s)
    cnt = 1
    ans = 0
    
    for x in range(1, n):
        if s[x] == s[x-1]:
            cnt += 1
        else:
            if cnt % 2== 0: ans += 1
            cnt = 1
    
    if cnt % 2 == 0: ans += 1
    print(ans)