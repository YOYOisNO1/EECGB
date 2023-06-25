    #!/usr/bin/python
    import os,math
    
    from sys import stdin, stdout
    A = []
    l = 0
    
    ma = 0
    hi = 0
    
def foo(req,P,d):
    	print(req,A)
    	global A,l,hi
    	
    	if d >= l:
    		if req <= hi:
    			return req;
    		return 
    	x = int(P[d])
    	val = req
    	ans = 0
    	if sum(A[:x+1]) == 0: # all previous ones are zero 
    		B = list(A)
    		for k in range(9,-1,-1):
    			while B[k] :
    				req *= 10
    				req += k
    				B[k] -= 1
    		if req <= hi:
    			ans = max(ans,req)
    		return ans;
    	else :
    		j = x-1
    		while A[j] == 0:
    			j -= 1
    		A[j] -= 1
    		req *= 10
    		req += j
    		B = list(A)
    		print(req,B)
    		for k in range(9,-1,-1):
    			while B[k] :
    				req *= 10
    				req += k
    				B[k] -= 1
    		if req <= hi:
    			ans = max(ans,req)
    		A[j] += 1
    		req = val;
    		if A[x] == 0:
    			return ans
    		else:
    			req *= 10;
    			req += x;
    			A[x] -= 1
    			ans = max(ans,foo(req,P,d+1))
    			A[x] += 1;
    			return ans
    			
    
def main():
    	global A,l,ma,hi
    	ten = [ 10**i for i in range(0,20) ]
    	"""
    	x = '123456789123456789\n'
    	y = '276193619183618162\n'
    	print(x)
    	print(y)
    	"""
    	x = stdin.readline()
    	y = stdin.readline()
    
    	if(len(y) > len(x)):
    		A = sorted([int(i) for i in x[:-1]],reverse=True)
    		A = map(str,A)
    		print(''.join(A))
    		return 
    	x = x[:-1]
    	y = y[:-1]
    	l = len(x)
    	A = [0]*10
    	hi = int(y)
    	ma = -1
    	for i in x :
    		A[int(i)] += 1
    
    	ma = foo(0,y,0)
    	print(ma)
    		
    if __name__=='__main__':
    	
    	main()
    	