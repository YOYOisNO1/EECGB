def program7962():
    n = int(input())
    num_likes = int(input())
    like = [ [] for u in range(n + 1) ]
    for i in range(num_likes):
        u, v = map(int, input().split())
        like[u].append(v)
        like[v].append(u)
    num_dislikes = int(input())
    dislike = [ (n + 1) * [ False ] for u in range(n + 1) ]
    for i in range(num_dislikes):
        u, v = map(int, input().split())
        dislike[u][v] = True
        dislike[v][u] = True
    result = 0
    
    seen = (n + 1) * [ False ]
    for u in range(1, n + 1):
        if seen[u]:
            continue
        seen[u] = True
        group = [ u ]
        queue = [ u ]
        tail = 0
        while tail < len(queue):
            u = queue[tail]
            tail += 1
            for v in like[u]:
                if seen[v]:
                    continue
                seen[v] = True
                group.append(v)
                queue.append(v)
        okay = True
        for i, u in enumerate(group):
            for j in range(i + 1, len(group)):
                v = group[j]
                if dislike[u][v]:
                    okay = False
                    break
            if not okay:
                break
        if okay:
            result = max(result, len(group))
    print(result)