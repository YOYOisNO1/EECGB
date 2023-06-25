def program3225():
    n, m = map(int, input().split())
    mp = dict()
    for _ in range(m):
        a, b = input().split()
        mp[a] = b;
    from itertools import product
    count = 0
    for t in product('abcdef', repeat=n) :
        s = ''.join(t)
        for _ in range(n - 1):
            s = mp.get(s[:2], 'g') + s[2:];
        if (s=='a'):
            count += 1
    print(count)
        