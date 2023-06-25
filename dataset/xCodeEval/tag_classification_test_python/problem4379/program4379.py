def program4379():
    import re
    s = input()
    s = s[0] + re.sub('dot', '.', s[1:-1]) + s[-1]
    s = s[0] + re.sub('at', '@', s[1:-1], count=1) + s[-1]
    print(s)