def program4443():
    s = input()
    l = len(s)
    ans = [s[0]]
    i = 1
    atdone = False
    while i < l:
        if i < l-3 and s[i:i+3] == "dot":
            ans.append(".")
            i += 3
        elif not atdone and s[i:i+2] == "at":
            ans.append("@")
            i += 2
            atdone = True
        else:
            ans.append(s[i])
            i += 1
    print('').join(ans)