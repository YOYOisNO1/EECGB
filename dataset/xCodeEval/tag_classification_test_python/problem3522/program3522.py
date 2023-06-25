def program3522():
    n, t = int(input()), input()[::2]
    print(max(t[:i].count('0') + t[i:].count('1') for i in range(n + 1)))