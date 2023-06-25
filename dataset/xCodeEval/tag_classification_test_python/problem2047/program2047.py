def f(k,n,d,b,l):
      if n<0 or b==0 and n<d: return 0
      elif l[n][b]>0: return l[n][b]
      else:
        cnt=0
        for i in range(1,k+1):
          if i<d: cnt+=f(k,n-i,d,b,l)
          else: cnt+=f(k,n-i,d,1,l)
        l[n][b]=cnt
        return cnt
    n,k,d=map(int,input().split())
    l=[[0,0] for i in range(n+1)]
    l[0]=[1,1]
    print((f(k,n,d,0,l)%1000000007))