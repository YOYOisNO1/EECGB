def program1356():
    a = int(input())
    b = int(input())
    c = int(input())
    m = []
    m.append(a+b+c)
    m.append(a*b+c)
    m.append(a*(b+c))
    m.append(a*b*c)
    m.append(a+b*c)
    m.append((a+b)*c)
    print(sorted(m)[len(m)-1])