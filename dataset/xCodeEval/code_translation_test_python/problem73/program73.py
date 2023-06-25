    import sys
    from math import floor, sqrt
    
    input = sys.stdin.readline
    
def main():
    	n, m = map(int, input().split())
    
    	rar = [-1]*(n+1)
    
    	for i in range(2, n+1):
    		if rar[i] == -1:
    			rar[i] = 1
    			curi = i*i
    			while curi <= n:
    				rar[i] += 1
    				rar[curi] = 0
    				curi *= i
    
    	ans = 0
    
    	check = [0] * (m*20 + 1)
    
    	kar = [0] * (21)
    
    	for k in range(1, 21):
    		for j in range(k, m*k + 1, k):
    			check[j] = 1
    		kar[k] = sum(check)
    
    	#print(kar)
    
    	for i in range(2, n+1):
    		if rar[i]:
    			ans += kar[rar[i]]
    
    
    				
    
    
    	#print(rar)
    
    	print(ans + 1)
    
    
    main()