def program1219():
    s = input()
    s = s[0] + s[1:].replace('at', '@', 1)
    print(s[0] + s[1:-1].replace('dot', '.') + s[-1])