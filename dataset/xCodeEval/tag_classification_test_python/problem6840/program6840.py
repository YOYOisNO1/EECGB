    res = {'': 1}
    
def valid(a):
        if len(a) == 2:
            return 1
        if a in res:
            return res[a]
        if (a[-1] == a[-3] or a[-2] == a[-4]):
            if (valid(a[:-4] + a[-2:])):
                res[a] = 1
                return 1
        if (len(a) > 7 and (a[-1] == a[-7] or a[-2] == a[-8])):
            if (valid(a[:-8] + a[-2:] + a[-6:-2])):
                res[a] = 1
                return 1
        res[a] = 0
        return 0
    
    n = int(input())
    s = input()
    s = s.replace(' ', '')
    print("YES" if valid(s) else "NO")