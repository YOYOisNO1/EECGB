def program3642():
    t = input()
    a = int(t[0]) + int(t[1]) + int(t[2: ]) if t[2] else -1
    b = int(t[0]) + int(t[1: -1]) + int(t[-1]) if t[1] else -1
    c = int(t[: -2]) + int(t[-2]) + int(t[-1])) if t[0] else -1
    print(max(a, b, c)