def program11():
    n = input()
    str1 = input()
    s = 0
    r = ''
    for i in range(1, n+1):
        r += str1[s:s+1]
        s += i
    print(r)