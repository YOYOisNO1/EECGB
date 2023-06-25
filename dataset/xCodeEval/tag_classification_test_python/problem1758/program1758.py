    t = int(input())
    A = [int(x) for x in input().split()]
    
    B = [-1 if a==0 else 1 for a in A]
    
def findMin(A):
    	N = len(A)
    	T = [0]*N
    	T[0] = A[0]
    	for i in range(1, N):
    		T[i] = A[i] + T[i-1] 
    
    	minsum = 0
    	for i in range(0, N):
    		for j in range(i, N):
    			sum = T[j]-T[i]+A[i]
    			if  sum < minsum:
    				minsum = sum 
    			#print("(%s,%s) = %s, minsum=%s") %(i,j,sum,minsum)
    	#print("Algorithm 2 : %s") % minsum
    	return minsum
    
def min_subarray(A):
        min_ending_here = min_so_far = 0
        for x in A:
            min_ending_here = min(0, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far
    
    sumA = sum(A)
    if sumA == t:
    	print(t-1)
    else:
    	print(sumA) + abs(min_subarray(B))
    