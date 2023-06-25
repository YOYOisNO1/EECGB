def program3104():
    R = lambda: map(int, input().split())
    s = input()
    cc, c = 0, 0
    for r in range(len(s)):
        if r == 0 or s[r] == s[r - 1]:
            c += 1
        else:
            cc += (c % 2 == 0)
            c = 1
    cc += (c % 2 == 0)
    print(cc)