    import sys
    import math
    
def readArray():return map(int,sys.stdin.readline().split())
def readString():return sys.stdin.readline().strip()
def readNum():return readString()
def exp(t,x):
       MOD=1000000007
       if(x==0):return 1
       if(x==1):return t
       if(x%2==1):return exp((t*t)%MOD,x/2)
def gcd(x,y):
       if x%y==0:return y
       else: return gcd(y,x%y)
def lcm(x,y):return x*(y/gcd(x,y))
def isprime(x):
       i=2
       while (i*i<=x):
          	if (x%i==0):return False
    	i+=1
       return True
    
    n,m,k=readArray()
    hoss=readArray()
    
    m-=1
    mn=n+1
    for i in range(n):
       if hoss[i]==0:continue
       if k>=hoss[i] and abs(m-i)<mn:mn=abs(m-i)
    
    print(mn*10)