def program940():
    from sys import stdin
    n = int(stdin.readline())
    a = stdin.readline().strip()
    pr = a[0]
    sf = 0
    fs = 0
    for i n a:
     if pr=='S' and i=='F':
      sf+=1
     elif pr=='F' and i=='S':
      fs += 1
     pr = i
    ans = 'NO'
    if sf > fs:
     ans = 'YES'
    print ans