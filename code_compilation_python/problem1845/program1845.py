    n=input()
    mp=''
def rec(s):
        global mp
        if len(s) == 2:
            if s==s[::-1]:
                mp = max(mp, s)
            mp = max(mp, max(s[1], s[0]))
            return
        for i in range(1, len(s)+1):
            rec(s[:i-1]+s[i:])
        if s==s[::-1]:
            mp = max(mp, s)
    rec(n)
    print(mp)