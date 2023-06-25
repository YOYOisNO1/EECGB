def program193():
    n,k=map(int, input().split()) 
    s=str(input())
    c=0;i=1
    while i<n: #i is ind of front lily
      if s[i:min(i+k,n)].count('1')==0:
        c=-1
        break
      else:
        i=k-s[min(i+k-1,n-1):i-1:-1].index('1')+i
        c+=1
    print(c)