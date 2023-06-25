def program5222():
    n=int(input())
    c=list(map(int,input()))
    m1=c[:n//2]
    m2=c[n//2:]
    
    if sum(m1)!=sum(m2):
    	print("NO")
    else:
    	if c.count(4)+c.count(7)==n:
    		print("YES")
    	else:
    		print("NO")
    		