def program677():
    from sys import stdin
    n,k = map(int,stdin.readline().split())
    a = map(int,stdin.readline().split())
    ans = 0
    for i in xrange(k):
     if i not in a:
      ans += 1
    ans += a.count(k)
    prnt ans