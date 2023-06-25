def program3274():
    import sys
    import math
    
    n = sys.stdin.readline()
    n = int(n)
    
    r1=0
    yes=True
    for i in range(n):
       x,d = sys.stdin.readline().split()
       x = int(x)
       if d[0]=='S':
          r1+=x
          if r1>20000:
    	 yes=False
    	 break
       elif d[0]=='N':
          r1-=x
          if r1<0:
    	yes=False
    	break
       else:
          if r1==0 or r1==20000:
    	 yes=False
    	 break
    
    if yes and r1==0:
       print('YES')
    else:
       print('NO')