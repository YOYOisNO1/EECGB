def program1955():
    n = int(input())
    a = int(input())
    b = int(input())
    sw = 0
    if b > a:
      a, b = b, a
      sw = 1
    ans = "NO"
    for i in xrange(n / a + 1):
      if (n - i * a) % b == 0:
        ans = "YES"
        break
    print(ans)
    if ans == "YES":
      if sw:
        print((n) - i * a) / b, i
      else:
        print(i,) (n - i * a) / b