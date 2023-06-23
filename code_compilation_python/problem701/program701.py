def program701():
    	'''input
    	3
    	0 1 3 5 6 8
    	1 2 4 5 7 8
    	2 3 4 6 7 9
    	'''
    	from itertools import permutations
    	n = input()
    	z = []
    	ans = []
    	for i in range(n):
    		tmp = map(int,input().split())
    		z.append(tmp)
    		for j in range(6):
    			ans.append(tmp[j])
    	if n == 1:
    		ans = list(set(ans))
    		ans.sort()
    		flag = False
    		if ans[0] == 0:
    			flag = True
    		cnt = 0
    		for i in range(len(ans)):
    			if flag:
    				if ans[i] == i:
    					cnt += 1
    				else:
    					break
    			else:
    				if ans[i] == i+1:
    					cnt += 1
    				else:
    					break
    		if flag:
    			print cnt-1
    		else:
    			print cnt
    
    
    	if n == 2:
    		for i in range(6):
    			for j in range(6):
    				m = int(str(z[0][i])+z[1][j])
    				mr = int(z[1][j]+z[0][i])
    				ans.append(m)
    				ans.append(mr)
    		ans = list(set(ans))
    		ans.sort()
    		flag = False
    		if ans[0] == 0:
    			flag = True
    		cnt = 0
    		for i in range(len(ans)):
    			if flag:
    				if ans[i] == i:
    					cnt += 1
    				else:
    					break
    			else:
    				if ans[i] == i+1:
    					cnt += 1
    				else:
    					break
    		if flag:
    			print cnt-1
    		else:
    			print cnt
    
    
    	if n == 3:
    		for i in range(6):
    			for j in range(6):
    				m = int(str(z[0][i])+str(z[1][j]))
    				mr = int(str(z[1][j])+str(z[0][i]))
    				ans.append(m)
    				ans.append(mr)
    		for i in range(6):
    			for j in range(6):
    				m = int(str(z[0][i])+str(z[2][j]))
    				mr = int(str(z[2][j])+str(z[0][i]))
    				ans.append(m)
    				ans.append(mr)
    		for i in range(6):
    			for j in range(6):
    				m = int(str(z[2][i])+str(z[1][j]))
    				mr = int(str(z[1][j])+str(z[2][i]))
    				ans.append(m)
    				ans.append(mr)
    		for i in range(6):
    			for j in range(6):
    				for k in range(6):
    					tmp = str(z[0][i])+str(z[1][j])+str(z[2][k])
    					perms = [''.join(p) for p in permutations(tmp)]
    					for kk in perms:
    						ans.append(int(kk))
    		ans = list(set(ans))
    		ans.sort()
    		flag = False
    		if ans[0] == 0:
    			flag = True
    		cnt = 0
    		for i in range(len(ans)):
    			if flag:
    				if ans[i] == i:
    					cnt += 1
    				else:
    					break
    			else:
    				if ans[i] == i+1:
    					cnt += 1
    				else:
    					break
    		if flag:
    			print cnt-1
    		else:
    			print cnt 
    
    
    
    
    
    
    
    