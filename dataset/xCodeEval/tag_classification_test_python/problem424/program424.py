    #!/usr/bin/env python
    
    
def Qsort(A) :
    	if len(A) <= 1:
    		return A
    	else :
    		return Qsort([i for i in A[1:] if i<A[0]]) + A[0:1] + Qsort([i for i in A[1:] if i>=A[0]])  
    
    if __name__ == "__main__":
    	S = [i for i in input()]
    	W = [i for i in input()]
    	X = [i for i in input()]
    	S = S + W
            S = sorted(S)
            X = sorted(X)
    	B = (len(S) == len(X))
    	if B :
    		for i in range(len(S)) :
    			if S[i] != X[i] :
    				B = False
    				break
    	if B :
    		print("YES")
    	else : 
    		print("NO")