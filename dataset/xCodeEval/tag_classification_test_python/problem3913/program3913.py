def program3913():
    w, m = map(int, input().split())
    for i in range(100, -1, -1):
      if abs(m - w**i) < m:
        m = abs(m - w**i)
    print('YES' if m == 0 else 'NO')