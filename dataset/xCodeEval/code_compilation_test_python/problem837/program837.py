def program837():
    a, b = map(int, input().split())
    ans = 0
    if a % b == 0 or b % a == 0:
      print(max(a // b, b // a))
      exit(0)
    while a and b:
      if a - b > 0:
        ans += a // b
        a, b = a % b, b
      else:
        ans += b // a
        a, b = a, b % a
    if a % b == 0:
      ans += a // b
    else:
      ans += b // a
    print(ans)