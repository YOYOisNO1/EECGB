def program358():
    ﻿n,x=map(int, input().split())
    counter=0
    for i in range(1,n+1):
     if x%i==0 and (x//i)<=n:
      counter+=1
     else:
      pass
      
    print(counter)