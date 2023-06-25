def program7964():
    t, p, k = [0] * (int(input()) + 1), {0: []}, 1
    for i in range(int(input())):
        a, b = map(int, input().split())
        if t[a] == t[b]:
            if t[a] == 0:
                t[a] = t[b] = k
                p[k] = [a, b]
                k += 1            
        else:
            if t[a] == 0:
                t[a] = t[b]
                p[t[b]].append(a)
            elif t[b] == 0:
                t[b] = t[a]
                p[t[a]].append(b)
            else:
                x, y = t[b], t[a]
                for c in p[x]:
                    t[c] = y
                p[y] += p[x]
                p[x] = []          
    for i in range(int(input())):
        a, b = map(int, input().split())
        if t[a] == t[b]: p[t[a]] = []
    ans = max(len(p[i]) for i in p)
    print(ans if ans > 0 else int(0 in t[1:]))