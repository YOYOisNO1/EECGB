    from collections import deque
    
def isgood(g):
        iss = False
        for i in g:
            if i == 0:
                if iss:
                    return False
            if i == 1:
                iss = True
        return True
    
    n = int(input())
    a = [int(x) for x in input().split()]
    o = deque()
    o.append(a.copy())
    vis = set()
    vis.add(tuple(a.copy()))
    ans = []
    maxans = -1
    while len(o) != 0:
        it = o.popleft()
        if len(it) > maxans:
            if isgood(it):
                l = len(it)
                ans.append(l)
                maxans = max(maxans, l)
            else:
                for i in range(len(it)):
                    tmp = it[:i] + it[i + 1:]
                    if tuple(tmp) not in vis:
                        o.append(tmp)
                        vis.add(tuple(tmp))
    print(max(ans))