def program519():
    import math
    l=list(map(int,input().split()))
    n=sum(l)/len(l)
    if n%1:
         print(-1)
    else:
         if n<=max(l):
              print(math.floor(n)
         else:
              print(-1)