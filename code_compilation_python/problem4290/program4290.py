def program4290():
    s = input()
    done = False
    for i in range(len(s)):
        for k in range(i):
            if s[:i] == s[k:]:
                done = True
                res = s[:i]
    if done:
        print("YES")
        print(res)
    else:
        print("NO")