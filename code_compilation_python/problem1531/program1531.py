def calc(n):
        ans=0    
        while n:
          t=int(n**(1/3)+0.0000000000001)
          n-=t*t*t
          ans+=1
        return ans
    n=int(input())
    print(' '.join(map(str,max([(calc(i),i) for i in range(n,max(n-1000000,0),-1)]))))