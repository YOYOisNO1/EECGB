def program3303():
    input()
    u, v = input(), input()
    print(['YES', 'NO'][any('^v'[i] + '<>'[j] == v[i] + u[j] for i in [0, -1] for j in [0, -1])])input()
    u, v = input(), input()
    a = [u[i] + v[j] for i in [0, -1] for j in [0, -1]]
    b = ['<^', '>^', '<v', '>v']
    print(['YES', 'NO'][any(i == j for i, j in zip(a, b))])