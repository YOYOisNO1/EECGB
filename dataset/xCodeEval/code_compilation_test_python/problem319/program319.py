def program319():
    import sys
    line = map(int, input().split())
    a = line[0]
    b = line[1]
    c = line[2]
    d = line[3]
    m = max(3 * a, a - a * c / 25)
    v = max(3 * b, b - b * d / 25)
    if (m > v): sys.stdout.write('Misha')
    elif (m < v): sys.stdout.write('Vasya')
    else: sys.stdout.write('Tie')