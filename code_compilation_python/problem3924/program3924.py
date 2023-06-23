def program3924():
    n = input().split()
    l = int(n[1])
    n = int(n[0])
    c = input().split()
    cperl = []
    for i in range(n):
        c[i] = int(c[i])
        cperl.append([(c[i])/2**i, 2**i, i])
    cperl.sort()
    f = False
    nl = [0]
    nc = [0]
    i = 0
    while not f:
        if nl[i] + cperl[i][1] == l:
            nl[i] += cperl[i][1]
            nc[i] += c[cperl[i][2]]
            f = True
        elif nl[i] + cperl[i][1] < l:
            nl[i] += cperl[i][1]
            nc[i] += c[cperl[i][2]]
        else:
            nl.append(nl[i])
            nc.append(nc[i])
            nl[i] += cperl[i][1]
            nc[i] += c[cperl[i][2]]
            i += 1
        if i == n:
            break
    print(min(nc))