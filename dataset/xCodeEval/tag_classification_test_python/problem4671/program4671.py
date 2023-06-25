def program4671():
    n,k = map(int, input().split())
    a = list(input())
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    m = {}
    given = {}
    for i in alp:
    	m[i] = -1
    	given[i] = 0
    for i in range(len(a)-1,-1,-1):
    	if(m[a[i]]==-1):
    		m[a[i]] = i
    gates = 0
    guards = k-1
    given[a[0]] = 1
    
    for i in range(0,len(a)):
    	if(given[a[i]]):
    		pass
    	else:
    		given[a[i]]=1
    		guards-=1
    	if(guards<0):
    		gates+=1
    		break
    	if(m[a[i]]==i):
    		guards+=1
    if(gates==1):
    	print("YES")
    else:
    	print("NO")