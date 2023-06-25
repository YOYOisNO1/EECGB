def program4525():
    was = [0] * 100010
    a, b, m, r = map(int, input().split())
    t = 1
    while 1:
        if was[r] == 0:
            was[r] = t
            t += 1
            r = (r*a + b) % m
        else:
            print(t-was[r])
            break