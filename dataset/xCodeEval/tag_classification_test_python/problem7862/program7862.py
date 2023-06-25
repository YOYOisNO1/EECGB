def program7862():
    n = input()
    m = input()
    lst = [int(x) for x in m.split(' ')]
    p = []
    ans = 0
    for i in range(0, len(lst)):
        while len(p) > 1 and lst[i] >= p[-1] and p[-2] >= p[-1]:
            ans += min(p[-2], lst[i])
            del(p[-1])
        p.append(lst[i])
    p.sort()
    #print(p)
    ans += sum(p[0:-2])
    print(ans)