def program2180():
    n, c = map(int, input().split(" "))
    p = map(int, input().split(" "))
    t = map(int, input().split(" "))
    clock = 0
    s1 = 0
    for i in xrange(n):
      clock += t[i]
      s1 += max(0, p[i] - c * clock)
    clock = 0
    s2 = 0
    for i in xrange(n - 1, -1, -1):
      clock += t[i]
      s2 += max(0, p[i] - c * clock)
    if s1 > s2:
      print("Limak")
    elif s1 < s2:
      print("Radewoosh")
    else:
      print("Tie")