def program833():
    from collections import Counter
    i, j, p, s = 0, 0, {(0, 0)}, input()
    for ch in s:
        i += [0, 0, -1, 1]['LRUD'.index(ch)]
        j += [-1, 1, 0, 0]['LRUD'.index(ch)]
        p.add((i, j))
    c = Counter(((x-1,y) in p)+((x+1,y) in p)+((x,y-1) in p)+((x,y+1) in p) for x,y in p)
    print('OK' if c[1] == 2 and c[2] == len(s) - 1 else 'BUG')