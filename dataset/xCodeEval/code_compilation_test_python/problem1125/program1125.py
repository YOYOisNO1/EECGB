    e=int(input()) 
def sieve(n): 
       save = [0] * (n+1) 
       save[0]=save[1]=1
       i = 2 
       while (i*i <= n): 
          if (save[i]): 
             k = i*i 
             while (k<=n): 
                save[k] =1
             k += i 
          i+= 1 
      return save
def prime(n):
       p=sieve(n) 
       l=[]
       for i in range(n+1):
          if p[i]==0:
             if n%i==0:
                l.append(i)
       return l
def ur(n):
       p=sieve(n) 
       q=prime(n) 
       if p[n]==0:
          return n+1
       else:
          return n+ur(n//q[0]) 
    print(ur(e)) 
    
     