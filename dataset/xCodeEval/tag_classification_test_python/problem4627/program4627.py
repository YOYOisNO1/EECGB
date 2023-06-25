def program4627():
    n, k = map(int, input().split())
    s = input()
    dic = dict()
    d = {}
    for i in set(s):
        dic[i] = s.rfind(i)
        d[i] = 1
    o = 0
    for i in range(len(s)):
        if d[s[i]]:
            o += 1
            if o > k: print('yes'); exit()
            d[s[i]] = 0
        if i == dic[s[i]]: o -= 1
    print('no')