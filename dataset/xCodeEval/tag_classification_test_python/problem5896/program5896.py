    import sys
    
    n = int(sys.stdin.readline())
    crash = map(lambda x: int(x) - 1, sys.stdin.readline().split(' '))
    
    lens = []
    was = [False] * n
    for x in crash:
        was[x] = True
    if not all(was):
        print(-1)
        exit()
    
    was = [False] * n
    
    for x in range(n):
        if not was[x]:
            y = crash[x]
            cur_len = 1
            was[x] = True
            while y != x:
                was[y] = True
                cur_len += 1
                y = crash[y]
            lens.append(cur_len)
    
    ans = 1
    for l in lens:
        if l % 2 == 0:
            l /= 2
    def lcm(a, b):
        def gcd(a, b):
                if b == 0:
                    return a
                return gcd(b, a % b)
            return a * b / gcd(a, b)
        ans = lcm(ans, l)
    print(ans)
    
    