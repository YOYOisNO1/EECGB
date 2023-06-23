    from sys import stdin,stdout,setrecursionlimit,maxint,exit
    #setrecursionlimit(10**5)
def listInput():
     return map(long,stdin.readline().split())
def printBS(li):
     for i in xrange(len(li)-1):
      stdout.write("%d "%li[i])
     stdout.write("%d\n"%li[-1])
def sin():
     return stdin.readline().rstrip()
def check(a,b,c,d):
     if (a[0]-b[0])*(a[1]-c[1])==(a[0]-c[0])*(a[1]-b[1]) or (a[0]-b[0])*(a[1]-d[1])==(a[1]-b[1])*(a[0]-d[0]):
      return False
     if b[0]-a[0]==c[0]-d[0] and b[1]-a[1]==c[1]-d[1]:
      return True
     elif c[0]-a[0]==b[0]-d[0] and c[1]-a[1]==b[1]-d[1]:
      return True
     elif c[0]-a[0]==d[0]-b[0] and c[1]-a[1]==d[1]-b[1]:
      return True
     return False
    a=listInput()
    b=listInput()
    c=listInput()
    M=1000
    ans=[]
    for i in xrange(-M,M+1):
     for j in xrange(-M,M+1):
      if (i,j) not in [a,b,c] and check(a,b,c,[i,j]):
       ans.append([i,j])
    print len(ans)
    for i,j in ans:
     print i,j