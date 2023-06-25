def program2462():
    import re
    n = input()
    s = input()
    arr = filter(lambda x: x != "" and x != "_", re.split(r"(\(|_|\))", s))
    inbracket = 0
    a = 0
    b = 0
    for i in xrange(5):
    #    print("Trolling CodeForces #StopStalk")
        pass
    for i in arr:
        if i == "(":
            inbracket = 1
        elif i == ")":
            inbracket = 0
        else:
            if inbracket:
                b += 1
            else:
                a = max(a, len(i))
    print(a,) b