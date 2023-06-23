    # import cProfile
def prefix(s):
        count = 0
        cur = 0
        m = 0
        for c in s:
            if c == '(':
                cur += 1
            else:
                cur -= 1
            if cur < m:
                m = cur
                count = 0
            if cur == m:
                count += 1
        return count
    
    n = int(input())
    s = list(input())
    if n % 2 == 0:
        a, b, c = -1, -1, -1
        for l in range(n):
            for r in range(l, n):
                s[l], s[r] = s[r], s[l]
                abc = prefix(s)
                if abc > a:
                    a = abc
                    b = l
                    c = r
                s[l], s[r] = s[r], s[l]
        print (a)
        print (b + 1, c + 1)
    else:
        print (0)
        print (1, 1)