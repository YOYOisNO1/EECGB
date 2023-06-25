def program3330():
    from collections import Counter
    inp = (input())
    r = inp.split(" ")
    
    for i in range(int(r[0]), int(r[1])+1):
        s = f"{i}"
        d = Counter(s)
        f = 0
        for x in d:
            if d[x] > 1:
                f = 1
        if f == 0:
            print(i)
            break
    else:
        print(f"{-1}")