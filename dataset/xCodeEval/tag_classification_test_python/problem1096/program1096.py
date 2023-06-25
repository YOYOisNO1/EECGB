def program1096():
    from itertools import permutations
    from copy import deepcopy
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(0, 0), (0, 2), (1, 1), (1, 0), (2, 2), (2, 1)]
    ans = 1e10
    minimum = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    for p in permutations(c):
        a1=deepcopy(a)
        b1=deepcopy(b)
        for i in range(0, len(p)):
            a1[p[i][0]] -= min(a1[p[i][0]], b1[p[i][1]])
            b1[p[i][1]] -= min(a1[p[i][0]], b1[p[i][1]])
    
        ans = min(ans, min(a1[0], b1[1]) + min(a1[1], b1[2]) + min(a1[2], b1[0]))
        # print(ans)
    print(ans, minimum)