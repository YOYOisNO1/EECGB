def program345():
    n = int(input())
    level = input()
    max_jump = n // 4 - 1
    found = False
    platforms = [i for i in range(n) if level[i] == '*']
    if not platforms:
    	print('no')
    else:
    	for platform in platforms:
    		for jump in range(1, max_jump):
    			try:
    				if level[platform + jump] == '*' and level[platform + jump*2] == '*' and level[platform + jump*3] == '*' and not found:
    					print('yes')
    					found = True
    			except:
    				break
    	if not found:
    		print('no')