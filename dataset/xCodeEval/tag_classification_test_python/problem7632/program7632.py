def program7632():
    s = input()
    n = len(s)
    x = int(s)
    m = int(input())
    t = 1
    cur = 0
    for i in range(n):
      cur += (ord(s[n - i - 1]) - 48) * t
      cur %= m
      t = (t * 10) % m
    ans = cur
    for i in range(n - 1):
      cur = cur * 10
      cur -= t * (ord(s[i]) - 48)
      cur += (ord(s[i]) - 48)
      cur %= m
      cur += m
      cur %= m
      if (s[i + 1] != '0'):
          ans = min(ans, cur)
    print(ans)