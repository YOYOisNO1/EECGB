def program413():
    # your code goes here
    from sys import stdin
    ar=map(int, stdin.readline().strip().split())
    n=ar[0]
    m=ar[1]
    
    if m<=n:
      t=(n/2)ifn%2==0 else (n/2)+1
      while t<=n:
        if t%m==0:
          print t
        else:
          t+=1
    else:
      print -1