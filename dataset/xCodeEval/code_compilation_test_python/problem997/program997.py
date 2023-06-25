def program997():
    n, pos = map(int, input().split(' '))
    a = map(int, input().split(' '))
    pos -= 1
    ans = a[pos]
    l = pos - 1
    r = pos + 1
    while l >= 0 or r < n:
      if l >= 0 and r < n:
        if a[l] == 1 and a[r] == 1:
          ans += 2
      elif l >= 0:
        if a[l] == 1:
          ans += 1
      else:
        if a[r] == 1:
          ans += 1
      l--
      r++
    print ans