def program486():
    n, k = map(int, input().split())
    s = input()
    g = s.index('G')
    t = s.index('T')
    if t < g:
       k = -k
    while True:
       g = g + k;
       if g >= n or g < 0:
           print("NO")
           break
       else:
           if s[g] == '#':
               print('NO')
               break
           elif s[g] == 'T':
               print('YES')
               break