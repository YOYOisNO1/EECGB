def program932():
    s = input()
    a = []
    for i in range(100):
        a.append(s)
        s = s[1:] + s[0]
    print(len(set(a)))