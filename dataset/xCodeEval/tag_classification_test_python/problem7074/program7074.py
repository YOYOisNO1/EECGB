def program7074():
    c,d = input().split()
    n,m = input().split()
    c,d = int(c), int(d)
    n,m = int(n), int(m)
    k = int(input())
    
    outp = 1000000000
    
    for i in range(1000000):
    	if((n*m-k-n*i)<0):
    		outp=min(outp,c*i)
    	else:
    		outp=min(outp,(n*m-k-n*i)*d+i*c)
    
    print(outp)