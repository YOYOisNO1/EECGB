def program391():
    s = input()
    try:
        i = s.index("1")
        if s[i:].count("0") >= 6:
            print("yes")
        else:
            print("no")
    except ValueError:
        print("no")