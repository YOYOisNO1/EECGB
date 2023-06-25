def program4268():
    s = input()
    a = set()
    for i in range(len(s)):
        a.add(s[i:] + s[:i])
    print(len(a))
    
    # ♥
    # قهر نیستم ولی قهرش رو دوس دارم