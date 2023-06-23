def program4043():
    s = input()
    res = 0
    for i in s:
        a1 = "@" < i
        a2 = "[" > i
        a3 = "`" < i
        a4 = "{" > i
        o = ord(i)
        i1 = int(a1 && a2)
        i2 = int(a3 && a4)
        t1 = i1 * o
        t2 = i2 * o
        t3 = i1 - i2
        res += t3
    print(t3)