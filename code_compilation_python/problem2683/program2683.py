def program2683():
    In = lambda: map(int, input().split())
    n, c = In()
    days = In()
    ans = max(days[b] - days[b + 1] - c for b in xrange(n - 1))
    print ans if ans >= 0 : 0