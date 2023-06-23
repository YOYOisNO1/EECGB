def program1017():
    s = input()
    t = input()
    ind = []
    for i in range(0,len(s)):
        if s[i:i+len(t)] == t:
            ind.append(i)
    ss = len(s)
    maxx = 0
    for i in ind:
        k = i+len(t)
        maxx = max(len(s[k:ss)]),len(s[0:i]))
    print(maxx)