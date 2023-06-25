def program4350():
    s = input()
    res = []
    for i in range(len(s)):
        if i == 0:
            res.append(i)
        elif i % 2 == 1:
            res.append(i)
        else:
            res = [i] + res
    result = ['' for _ in range(len(s))]
    for i in range(len(res)):
        result[res[i]]=s[i]
    print('').join(result)
        