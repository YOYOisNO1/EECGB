def calculaFatorial(n):
    	if n == 0 or n==1:
    		return 1
    	else:
    		return n* calculaFatorial(n-1)
        
    n = map(int,input().split(" "))
    n.sort()
    
    print(calculaFatorial(n[0]))