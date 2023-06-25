def program2709():
    [n] = input().split()
    n = int (n)
    v = []
    for i in range (n) :
      v.append(0)
    v = input().split()
    mx = int (-1)
    votes = int (0)
    for x in v :
      x = int (x)
      mx = max (mx, x)
      votes += x
    votes = n * mx - votes
    while (votes < n * mx - votes) :
      mx = mx + 1
    print mx 