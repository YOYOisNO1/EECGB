def program4646():
    #834B
    n, k = map(int, input().split(" "))
    s = input()
    # ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # alpha = [0]*(n+1)
    # for i in ref:
    #     if i in s:
    #         alpha[s.index(i)] += 1
    #         alpha[s.rindex(i)+1] -= 1
    # print(alpha)
    
    # h = 0
    # for j in range(n):
    #     h += alpha[j]
    #     if h>k:
    #         print('YES')
    #         break
    # else:
    #     print('NO')
    
    last_pos = {}
    active = set()
        
    for i in range(n):
        last_pos[s[i]] = i
    
    for i in range(n):
        active.add(s[i])
        if len(active) > k:
            print('YES')
            exit()
        if last_pos[s[i]] == i:
            active.remove(s[i])
    print('NO')