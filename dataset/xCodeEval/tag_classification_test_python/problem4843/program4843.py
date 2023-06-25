def program4843():
    inp = input().split()
    n = int(inp[0])
    s = int(inp[1])
    r = 0
    while(n > 0):
        c = int(s/n)
        r += c
        s -= c * n
        if s == 0:
            break
        n -= 1
    print(r)