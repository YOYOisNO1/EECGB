def program4479():
    
    n = int(input())
    cnt = [1 for k in range(10)]
    tot = 1
    
    while tot < n:
        for j in range(10):
            if tot >= n:
                break
            tot //= cnt[j]
            cnt[j] += 1
            tot *= cnt[j]
    
    cf = "codeforces"
    st = ""
    i = 0
    
    for c in cf:
        st += (c * cnt[i])
        i += 1
    
    print(st)
    