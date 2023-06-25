    from sys import stdin,stdout,setrecursionlimit,maxint,exit
    #setrecursionlimit(2*10**5)
def listInput():
     return map(long,stdin.readline().split())
def printBS(li):
     for i in xrange(len(li)-1):
      stdout.write("%d "%li[i])
     stdout.write("%d\n"%li[-1])
    s=stdin.readline().strip()
    res=""
    for i in s:
     if i in "aeiouyAEIOYU":
      continue
     if ord(i)>=65 and ord(i)<97:
      res+="."+chr(ord(i)-65+97)
     else: res+="."+i
    print(res)