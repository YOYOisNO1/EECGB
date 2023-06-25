def program4136():
    n, m = [int(x) for x in input().split()]
    E = {v: {v} for v in range(1, n+1)}
    for e in range(m):
        u, v = [int(x) for x in input().split()]
        E[u].add(v)
        E[v].add(u)
    if n > 400: print('ok')
    A = []
    letter = [None for i in range(n)]
    s = ''
    k = iter('ac')
    for v in E:
        for i, p in enumerate(A):
            if E[v] == p:
                letter[v-1] = s[i]
                break
        else:
            if len(A) < 3:
                A.append(E[v])
                s = s + 'b' if len(E[v]) == n else s + next(k)
                letter[v-1] = s[-1]
            else:
                print("No")
                break
    else:
        print("Yes")
        print(''.join(letter))
        
        