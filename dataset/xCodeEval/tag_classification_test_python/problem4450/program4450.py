def program4450():
    t = input()
    t = t[0] + t[1: -1].replace('dot', '.') + t[-1]
    k = t.find('at', 1)
    print(t[:k] + '@' + t[k + 2:])