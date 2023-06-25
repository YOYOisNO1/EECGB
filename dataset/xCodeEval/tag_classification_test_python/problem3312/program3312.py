def program3312():
    R = lambda: map(int, input().split())
    n, m, r = R()
    s, b = min(R()), max(R())
    print(r) % s + r / s * b if s < b else r