    from sys import stdin,stdout,setrecursionlimit,maxint,exit
    setrecursionlimit(10**5)
def listInput():
     return map(long,stdin.readline().split())
def printBS(li):
     for i in xrange(len(li)-1):
      stdout.write("%d "%li[i])
     stdout.write("%d\n"%li[-1])
def sin():
     return stdin.readline().rstrip()
def solve(m,w):
     no=[]
     t=m
     while t!=0:
      no.append(t%w)
      t/=w
     i=0
     while i<len(no):
      if no[i] in (0,1): 
       i+=1
       continue
      if (no[i]-w) in (0,-1,1):
       if i==len(no)-1: no.append(1)
       else: no[i+1]+=1
       i+=1
      else: return False
     return True
    w,m=listInput()
    if solve(m,w): print("YES")
    else: print("NO")