def program7961():
    n = int(input())
    l = int(input())
    likes_list = [[] for i in range(n + 1)]
    for i in range(l):
        a, b = map(int, input().split())
        likes_list[a].append(b)
        likes_list[b].append(a)
    
    d = int(input())
    dislikes_list = [[] for i in range(n + 1)]
    for i in range(d):
        a, b = map(int, input().split())
        dislikes_list[a].append(b)
        dislikes_list[b].append(a)
    
    v = [False] * (n + 1)
    groups = {}
    f_id = [i for i in range(n + 1)]
    
    for i in range(1, n + 1):
        if not v[i]:
            f = set()
            s = [i]
            while len(s) > 0:
                x = s.pop()
                f_id[x] = i
                f.add(x)
                if v[x]:
                    continue
                v[x] = True
                for y in likes_list[x]:
                    s.append(y)
            groups[i] = f
    
    for i in range(1, n + 1):
        for ds in dislikes_list[i]:
            groups[f_id[i]].difference_update({ds}.union(groups[f_id[ds]]))
    
    ans = 0
    for v in groups.values():
        ans = max(ans, len(v))
    print(ans)