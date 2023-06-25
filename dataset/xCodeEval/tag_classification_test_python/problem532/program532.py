def program532():
    n, x = map(int, input().split())
    s = map(int, input().split())
    ans = 0
    for i in range(101):
      if i > x:
        break
      if i < x and i not in s:
        ans += 1
      elif i == x and i in s:
        ans += 1
    print(ans)    