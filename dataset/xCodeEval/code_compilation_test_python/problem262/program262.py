def program262():
    w = input()
    ind = True
    alf = ["a", "e", "i", "o", "u", "y"]
    while (ind):
        for i in range(len(w)):
            if i >= len(w):
                break
            if w[i] in alf:
                if w[i + 1] in alf:
                    w = w.replace(w[i + 1], "");
                    ind = False
    print(w)