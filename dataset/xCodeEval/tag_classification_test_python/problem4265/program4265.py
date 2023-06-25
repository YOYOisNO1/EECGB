def program4265():
    s = input()
    c_dict = set([s])
    for i in range(len(s)):
        s = s[1:] + s[0]
        c_dict.add(s)
    print(len(c_dict))