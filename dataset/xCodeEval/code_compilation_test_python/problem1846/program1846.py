    n=input()
    mp=''
def rec(s):
        global mp
        if s == '':
            return
        for i in range(1, len(s)):
            rec(s[:i-1]+s[i:])
        if s==s[::-1]:
            mp = max(mp, s)
    rec(n)
    print(mp)