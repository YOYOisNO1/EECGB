    import sys
    
    n = sys.stdin.readline()
    arr = map(int,sys.stdin.readline().split())
    
    n=int(n)
def gcd(a, b):
        """Return greatest common divisor using Euclid's Algorithm."""
        while b:      
            a, b = b, a % b
        return a
    
def lcm(a, b):
        """Return lowest common multiple."""
        return a * b // gcd(a, b)
    
    
    
    cont=[]
    for i in range(n):
      cont=cont+[0]
    keys=[]
    failed=False
    for i in range(n):
      if cont[i]==0:
        start=i
        k=0
        while cont[start]==0:
    	k=k+1
    	cont[start]=1
    	start=arr[start]-1
    	if start==i:
    	   break
    	if cont[start]>0:
    	   failed=True
    	   break
        if failed:
    	break
        keys=keys+[k]
    
    if failed:
       print(-1)
    else:
      res=1
      for k in keys:
       if k%2==0:
    	t=k/2
       else:
    	t=k
       res=lcm(res,t)
    
      print(res)