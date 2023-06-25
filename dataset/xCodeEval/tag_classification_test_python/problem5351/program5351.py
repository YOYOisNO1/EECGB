def program5351():
    t = 27 * [0]
    t[0] = 1
    s = map(lambda x:ord(x) - 96, input())
    ans = "YES"
    for i in s:
      if t[i-1] == 0:
        ans = "NO"
        break
      t[i] = 1
    print(ans)