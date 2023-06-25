def program4087():
    n = input()
    m = input()
    lst = [int(x) for x in m.split(' ')]
    p = []
    ans = 0
    for i in range(0, len(lst)):
        p.append(lst[i])
        if i-2 >=0 and lst[i] > lst[i-1] and lst[i-2] > lst[i-1]:
            del(p[-2])
            ans += min(lst[i], lst[i-2])
    p.sort()
    #print p
    for i in range(0, len(p)-2):
        ans += p[i]
    print ans