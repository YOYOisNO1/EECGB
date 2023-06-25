    #derangement permutation
    n,k=map(int,input().split())
    lst=[9,2,1,1]
def fac(n):
      l=[]
      s=1
      for i in range(1,2002):
        l.append(s)
        s=s*i  
      return l[n] 
    #f=fac()
    ans=0
    for j in range(1,k+1):
      ans=ans+(fac(n)/(fac(n-j)*fac(j)))*lst[4-j]
     # print(ans,(fac(n)/(fac(n-j)*fac(j))))
    print(ans-n+1)