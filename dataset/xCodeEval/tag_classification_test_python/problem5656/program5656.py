    from math import factorial as f
    
def b8(n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 7)
            nums.append(str(r))
        return ''.join(reversed(nums))
    
    n, m = map(int, input().split())
    
    n8 = b8(n-1)
    m8 = b8(m-1)
    
def isvalid(t, n8, m8):
        if len(t) <= len(n8):
            return t <= n8[:len(t)]
        else:
            return t[len(n8):] <= m8
    
def bf(t, n8, m8, i, unused):
        if i == len(n8+m8):
            #print(t)
            c = 1
        else:
            c = 0
            for ui in unused:
                tt = t + ui
                if isvalid(tt, n8, m8):
                    c += bf(tt, n8, m8, i+1, unused - {ui})
        return c
    
    if len(n8 + m8) > 7:
        sol = 0
    else:
        sol = bf('', n8, m8, 0, set([str(i) for i in range(7)]))
    print(sol)