def program500():
    a, b, x = (int(n) for n in input().split(" "))
    if a > b:
        s = "0"
        a -= 1
    else:
        s = "1"
        b -= 1
    for i in range(x - 1):
        if s[-1] == "0":
            s += "1"
            b -= 1
        else:
            s += "0"
            a -= 1
    if s[-1] == "0":
        s += a * "0"
        s += b * "1"
    else:
        s += b * "1"
        s += a * "0"
    print(s)