def program622():
    n=input()
    lst=map(int,input().split())
    s=31
    lst2=[]
    lst2=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lst3=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans=-1
    #print(lst2)
    for k in range(0,24):
      c=0
      c1=0
      for j in range(0,n):
        i=k
        
        i=(i+1)%24 
        #print(lst[j],lst2[(k+j)%24],k)
        if lst[j]==lst2[(k+j)%24]:
          c=c+1 
        if lst[j]==lst3[(k+j)%24]:
          c1=c1+1
     # print(c)
          
          
      if c==n or c1==n:
        print("yes")
        ans=0
        break 
    if ans==-1:
      print("no")