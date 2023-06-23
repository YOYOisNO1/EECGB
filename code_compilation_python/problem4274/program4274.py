def program4274():
    from sys import stdin
    s,x = map(int,stdin.readline().strip())
    y = x
    bi = 0
    while y>0:
     bi++
     y = y&(y-1)
    ans = pow(2,y)
    if s==x:
     ans-=2
    r = s-2*x
    if r%2:
     ans = 0
    print ans