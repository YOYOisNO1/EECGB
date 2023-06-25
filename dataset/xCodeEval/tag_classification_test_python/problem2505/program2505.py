def program2505():
    # your code goes here
    from __future__ import division 
    import sys 
    import math
    a,b,c,=map(long,sys.stdin.readline().split())
    if c!=0:
    	if (b-a)%c==0 and (b-a)/c>=0:
    		print("YES")
    	else:
    		print("NO")
    else:
    	if a==b:
    		print("YES")
    	else:
    		print("NO")