def program3970():
    w, m = map(int, input().split(" "))
    an = []
    while m != 0:
        mod = m % w
        m //= w
        an.append(mod)
    an += [0] * 100
    for _ in range(100):
        for i in range(100):
            an[i + 1] += an[i] // w
            an[i] %= w
            if an[i] == w - 1:
                an[i] = -1
                an[i + 1] += 1
    
    if all(map(lambda x: x == 0 or x == 1 or x == -1, an)):
        print("YES")
    else:
        print("NO")