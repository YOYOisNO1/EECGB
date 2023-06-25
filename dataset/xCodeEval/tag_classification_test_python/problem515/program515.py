def func(n,k,s):
    	x = [s]
    	cost = 0
    	while(len(x) < k):
    		for string in x:
    			l = len(string)
    			for j in range(l):
    				t = string[:j] + string[j+1:]
    				if(t == "" and t in x):
    					return -1
    				if(t not in x):
    					x.append(t)
    					cost += n - len(t)
    					if(len(x) >= k):
    						return cost
    	return cost
    a = [int(i) for i in input().split()]
    n = a[0]
    k = a[1]
    s = str(input())
    print(func(n,k,s))