    from sys import stdin
def ch(s):
     t = ''+s
     t.reverse()
     return t==s
    x = stdin.readline().strip()
    l = len(x)
    ans = 'NA'
    y = 'abcdefghijklmnopqrstuvwxyz'
    for i in xrange(l):
     fir = [0:i] 
     sec = [i:l]
     for j in y:
      nn = fir + y + sec
      if ch(nn):
       ans = nn
    print ans
     