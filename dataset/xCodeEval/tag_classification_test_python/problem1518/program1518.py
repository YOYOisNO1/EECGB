    cache = {}
    
def foo(a):
        n = len(a)
        if n == 1:
            return {a}
    
        if a in cache:
            return cache[a]
    
        s = set()
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    x = a[:i] + a[i + 1:j] + a[j + 1:]
                    s = s.union(foo(x + a[i]))
                else:
                    x = a[:i] + a[i + 1:j] + a[j + 1:]
                    s = s.union(foo(x + diff(a[i], a[j])))
        cache[a] = s
        return s
    
def diff(x, y):
        s = {x, y}
        return list({'R', 'G', 'B'} - s)[0]
    
    n = int(input())
    s = input().strip()
    t = []
    for i in s:
        if t.count(i) <= 2:
            t.append(i)
    
    t = "".join(t)
    s = foo(t)
    s = sorted(list(s))
    print("".join(s))