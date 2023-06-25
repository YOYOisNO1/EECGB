def program6064():
    
    from collections import defaultdict
    
    n = int(input())
    l = []
    d = defaultdict(list)
    for i in range(1,6):
    	for j in range(i+1,6):
    		for k in range(j+1,6):
    			l.append((i,j,k))
    
    # print(len(l))
    for i in range(n):
    	u,v = map(int,input().split())
    	d[u].append(v)
    	d[v].append(u)
    
    for i in l:
    
    	if i[0] in d[i[1]] and i[0] in d[i[2]] and i[1] in d[i[2]]:
    		print("WIN")
    		exit()
    	elif i[0] not in d[i[1]] and i[0] not in d[i[2]] and i[1] not in d[i[2]]:
    		print("WIN")
    		exit()
    print("FAIL")