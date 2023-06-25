def program3217():
    s = str(input())
    x = s[0]
    x = x.upper()
    s = s.replace(s[0], x, 1)
    print(s)