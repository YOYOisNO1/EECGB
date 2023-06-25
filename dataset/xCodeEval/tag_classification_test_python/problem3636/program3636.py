def program3636():
    n,t = map(int, input().split())
    q = list(input())
    for i in range(t):
      j = 0
      while j + 1 < n:
        if (q[j], q[j + 1]) == ('B', 'G'):
          q[j], q[j + 1] = 'G', 'B'
          j += 1
        j += 1
    print(''.join(q))