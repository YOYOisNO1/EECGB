def program3198():
    n=eval(input())
    a=eval(input())
    if n==1 or n==2 :
      print (-1)
      else:
        i=0
        j=100
        while i<n :
          a[i]=j
          i+=1
          j-=1
        print (a)  