def program2837():
    a = input()
    b = input()1
    l = len(a)
    s = ""
    for i in range(0,l):
        ed = 0
        if a[i] == "1":
            ed = ed + 1
        if b[i] == "1":
            ed = ed + 1
        if ed == 1:
            s = s + "1"
        else:
            s = s + "0"
    print s