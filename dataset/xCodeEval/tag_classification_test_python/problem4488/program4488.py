def program4488():
    """https://codeforces.com/contest/1042/problem/A"""
    from sys import stdin, stdout
    import math
    n = int(stdin.readline())
    m = int(stdin.readline())
    cap = [ int(line) for line in stdin ]
    total = m+sum(cap)
    best_each = math.ceil( total/n )
    mi,mx = best_each,0
    for c in cap:
        mi = max(mi,c)
        mx = max(mx,c+m)
    stdout.write(f"{mi} {mx}")