def program230():
    from collections import defaultdict
    
    t = int(input())
    for _ in range(t):
        n, k, d = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
    
        s = set(a[:d])
        dd = defaultdict(int)
        for i in a[:d]:
            dd[i] += 1
        mn = len(s)
        for i in range(n - d):
            #print(i, a[i], a[i+d], s)
            dd[a[i]] -= 1
            dd[a[i+d]] += 1
            s.add(a[i+d])
            if dd[a[i]] <= 0:
                dd[a[i]] = 0
                s.remove(a[i])
            m = len(s)
            #print(s, len(s))
            if m < mn:
                mn = m
        print(mn)