def program4660():
    n, k = map(int, input().split())
    s = list(input())
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    quards = {letters[i]: 0 for i in range(26)}
    
    for i in range(n):
        quards[s[i]] += 1
    
    d = []
    for key, value in quards.items():
        if not value:
            d.append(key)
    for key in d:
        del quards[key]
    
    ready = k
    now = []
    flag = True
    for man in s:
        # print(man, now, ready)
        if man not in now:
            if ready:
                ready -= 1
                now.append(man)
            else:
                print('YES')
                flag = False
                break
        quards[man] -= 1
        if not quards[man]:
            ready += 1
            now.remove(man)
        # print(quards, ready, now)
        # print()
    if flag:
        print('NO')