def program4374():
    s = input()
    res_s = ""
    if s[0:2] == "at":
        s = s[2:]
        res_s += "at"
    elif s[0:3] == "dot":
        s = s[3:]
        res_s += "dot"
    i = 0
    n = len(s)
    flag = False
    while i != len(s):
        done = False
        try:
            if s[i:i + 2] == "at" and i != n - 2 and not flag:
                i += 2
                res_s += "@"
                flag = True
                done = True
            elif s[i:i + 3] == "dot" and i != n - 3:
                i += 3
                res_s += "."
                done = True
        except:
            pass
        if done:
            continue
        res_s += s[i]
        i += 1
    print(res_s)