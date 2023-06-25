def program4060():
    line = input()
    ab, d = line.split('e')
    a, b = ab.split('.')
    d = int(d)
    newA = a + b[:d]
    newB = b[d:]
    if (d > len(b)):
        newA += (d - len(b)) * '0'
    while (newA[0:1] == '0'):
        newA = newA[1:]
    while (newB[-1:] == '0'):
        newB = newB[:-1]
    if newA == "":
        newA = '0'
    if newB == "":
        s = newA
    else:
        s = newA + "." + newB
    print(s)