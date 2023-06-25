def program2185():
    n=eval(input())
    e=1
    c=1
    while(e!=n):
      while(e<n):
        e=e*2
      if(e==n):
        e=n
      elif(e//2+1==n):
        c+=1
        e=n
      else:
        n=n-e//2
        c+=1
        e=1
    print(c) 