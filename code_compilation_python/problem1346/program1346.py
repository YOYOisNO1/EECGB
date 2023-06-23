def program1346():
    w = str(input())
    x = w.split("+")
    x = [z[i] = int(z[i]) for z in range(x)]
    x.sort
    nw = ""
    for n in x:
        nw += str(n) + "+"
    print(nw[:len(nw) -1])