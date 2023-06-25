def program6536():
    n = int(input())
    s = [1 if c == '(' else -1 for c in input()]
    if s.count(1) != s.count(-1):
        print(0)
        print(1, 1)
        exit()
    
    ans = 0
    pair = 1, 1
    for i in range(n-1):
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            min_p, cnt = 10**9, 0
            nest = 0
            for k in range(n):
                nest += s[k]
                if min_p > nest:
                    min_p = nest
                    cnt = 1
                elif min_p == nest:
                    cnt += 1
    
            if ans < cnt:
                ans = cnt
                pair = i+1, j+1
    
            s[i], s[j] = s[j], s[i]
    
    print(ans)
    print(*pair)