def program492():
    x = input()
    if len(x) < 7:
        print("no")
        exit(0)
    c = 0
    fl = 0
    for i in x:
        if i == "1":
            fl = 1
        if i == "0" and fl == 1:
            c += 1
    if c >= 6:
        print("yes")
        exit()
    print("no")