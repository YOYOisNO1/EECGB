def program7380():
    n, m = [int(x) for x in input().split()]
    E = {v: {v} for v in range(1, n+1)}
    for e in range(m):
        u, v = [int(x) for x in input().split()]
        E[u].add(v)
        E[v].add(u)
    A = []
    letter = [None for i in range(n)]
    s = ''
    k = iter('acx')
    for v in E:
        for i, p in enumerate(A):
            if E[v] == p:
                letter[v-1] = s[i]
                break
        else:
            if len(A) < 3:
                A.append(E[v])
                s = s + 'b' if len(E[v]) == n else s + next(k)
                if s[-1] == 'x':
                    print("No")
                    break
                letter[v-1] = s[-1]
            else:
                print("No")
                break
    else:
        print("Yes")
        print(''.join(letter))
        
        