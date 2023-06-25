    '''input
    8
    7954 0 1
    5638 0 1
    8204 0 2
    8293 1 1
    3598 0 1
    0894 0 1
    6324 1 2
    0572 0 1
    '''
    from sys import stdin, setrecursionlimit
    import math
    from collections import defaultdict, deque
    import time
    from itertools import combinations, permutations
    from copy import deepcopy
    
    setrecursionlimit(15000)
    
    
def take_intersection():
    	pass
    
def discover_digits(guess):
    	myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    	flag = 0
    	count = 0
    	final = []
    	comb = permutations(myset, 4)
    	for i in comb:
    		ans = get_answer(guess, list(i))
    		if len(ans) == 4:
    			count += 1
    			final.append(ans)
    			flag = 1
    
    	if count == 1:
    		for i in final[0]:
    			print(i, end = '')
    	elif count > 1:
    		print("Need more data")
    	if flag == 0:
    		print("Incorrect data")
    
    
def check(arr, guess, index):
    	first = 0
    	total = 0
    	second = 0
    	for i in range(4):
    		if arr[i] == int(guess[index][0][i]):
    			first += 1
    		if str(arr[i]) in guess[index][0]:
    			total += 1
    	second = total - first
    	if first == int(guess[index][1]) and second == int(guess[index][2]):
    		return True
    	else:
    		return False
    
    
def get_answer(guess, answer):
    	flag = 0
    	ans = []
    	for j in range(len(guess)):
    		num = guess[j][0]
    		if check(answer, guess, j):
    			pass
    		else:
    			break
    	else:
    		ans = answer
    
    	return ans
    
    
    # main starts
    n = int(stdin.readline().strip())
    guess = []
    for _ in range(n):
    	guess.append(list(map(str, stdin.readline().split())))
    
    
    # getting ready final list
    final = []
    base = set()
    discover_digits(guess)