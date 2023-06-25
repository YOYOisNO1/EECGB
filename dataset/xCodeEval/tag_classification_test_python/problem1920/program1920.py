    from sys import stdin,stdout,setrecursionlimit,maxint
    setrecursionlimit(2*10**5)
def listInput():
     return map(long,stdin.readline().split())
def printBS(li):
     for i in xrange(len(li)-1):
      stdout.write("%d "%li[i])
     stdout.write("%d\n"%li[-1])
def sin(): return stdin.readline().rstrip()
    #from fractions import gcd
    n=int(sin())
    if n==1: print(1)
    elif n==2: print(2)
    elif n==3: print(6)
    elif n%2==1:
     print(n*(n-1)*(n-2))
    else:
     if n%3==0: print((n-1)*(n-2)*(n-3))
     else: print((n-1)*(n-3)*n)