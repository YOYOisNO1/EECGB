def program2014():
    N = int(input())
    
    M = map(int,input().split(' '))
    R = map(int,input().split(' '))
    
    n = 10000000
    
    results = list()
    
    for i in range(N):
    	result = set()
    	for D in range(1,n+1):
    		if D % M[i] == R[i]:
    			result.add(D)
    	results.append(result)
    
    ans = reduce(lambda a,b: a.union(b), results)
    
    print(len(ans)/float(n))