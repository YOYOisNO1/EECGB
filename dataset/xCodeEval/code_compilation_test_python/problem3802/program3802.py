def program3802():
    
     list = [int(number) for number in input().split()]
    n, k = list[0], spisok[1]
    cc = [int(o) for o in input().split()]
    
    d = dict()
    for c in cc:
        d[c] = d.get(c, 0) + 1
    m = max(d.values())
    nb = m // k
    if m % k != 0:
        nb += 1
    print(nb * len(d) * k - n)