def program4090():
    n = input()
    m = input()
    lst = [int(x) for x in m.split(' ')]
    p = []
    for i in range(1, len(lst)-1):
        p.append(min(lst[i-1], lst[i+1]))
    ans = 0
    while len(p) > 0:
        id = p.index(max(p))
        ans += max(p)
        if id-1 >= 0 and id+2 < len(lst):
            p[id-1] = min(lst[id-1], lst[id+2])
        if id+1 < len(p) and id+3 < len(lst):
            p[id+1] = min(lst[id], lst[id+3])
        del(p[id])
        del(lst[id+1])
    print ans