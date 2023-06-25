def program162():
    n,s = input().split()
    
    n,s = int(n), int(s)
    tot=0
    x=input().split()
    
    m = int(max(i for i in x))
    
    for i in x:
    	tot+=int(i)
    
    if(tot-m<=s):
    	print("YES")
    else:
    	print("NO")