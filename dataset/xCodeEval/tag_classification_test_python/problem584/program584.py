def nums():
        return map(int, input().split())
    p = nums()
    x1, y1, z1 = nums()
    a = nums()
    nps = [((0, -1, 0), (0, 0, 0)), ((0, 1, 0), (0, y1, 0)),
            ((0, 0, -1), (0, 0, 0)), ((0, 0, 1), (0, 0, z1)),
            ((-1, 0, 0), (0, 0, 0)), ((1, 0, 0), (x1, 0, 0))]
def func(p, n, p0):
        return sum(Ai*(xi-x0i) for Ai, xi, x0i in zip(n, p, p0))
    print(sum(ai) for (n, p0), ai in zip(nps, a) if func(p, n, p0) > 0)