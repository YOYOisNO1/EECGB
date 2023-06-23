def program238():
    n = int(input())
    s = input()
    bul = False
    x, d = 1, 0
    r, g, b = "R", "G", "B"
    rn, gn, bn = s.count(r), s.count(g), s.count(b)
    lista = list()
    if len(s) == 1:
        print(x - 1)
    elif len(s) == 2:
            if s[0] != s[1]:
                print(x - 1)
            else:
                print(x)
    else:
        if n == (rn or gn or bn):
            print(n-1)
        elif n == (rn + gn or gn + bn or bn + rn):
            print(n-2)
        else:
            while x < n-1:
                if s[x] != (s[x - 1] and s[x + 1]):
                    print(0)
                    break
                else:
                    y = 0
                    z = n - 1
                    while 0 <= y < x:
                        if s[x] != s[y]:
                            d += x-y
                        else:
                            y += 1
                    while x < z < n:
                        if s[x] != s[z]:
                            d += x-y
                        else:
                            z -= 1
                    lista.append(d)
                    print(min(lista))
                x += 1