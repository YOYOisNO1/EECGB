def program3569():
    t = int(input().split(' ')[1])
    q = input()
    for _ in range(t):
      n = q.replace('BG', 'GB')
      if n is q:
        break
      else:
        q = n
    print(q)