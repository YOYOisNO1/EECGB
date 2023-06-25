    #---------------EL FUTURO ES INCIERTO--------------#
    
    import sys
    
def gcd(a,b):
        if(b == 0):
            return a
        else:
            return gcd(b, a%b)
    
    INF = 100000000
    
    n = int(input())
    arr = [int(x) for x in input().split()]
    id = 1;
    mat = [[int(INF) for _ in range(0,n+2)] for _ in range(0,n+2)]
    
    for u in arr:
    	mat[id][u] = 1
    	id+=1
    
    for k in range(1,n+1):
    	for i in range(1,n+1):
    		for j in range(1,n+1):
    			mat[i][j] = min(mat[i][j],mat[i][k] + mat[k][j])
    
    fine = 1
    ss = []
    for i in range(1,n+1):
    	if(mat[i][i] == INF):
    		fine = 0
    		break
    	else:
    		k = mat[i][i]
    		if(k%2 == 0):
    			k /=2
    		ss.append(k)
    #end for
    
    if(fine == 0):
    	print(-1)
    else:
    	ans = 1
    	for u in ss:
    		ans = ans*u/gcd(ans,u)
    	print(int(ans))