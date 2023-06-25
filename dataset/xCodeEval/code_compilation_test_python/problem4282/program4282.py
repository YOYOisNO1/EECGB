def oth_el(a, i):
    	return a[i+1-i % 2*2]
    
    
def oth_el2(a1, x1):
    	return oth_el(a1, a1.index(x1))
    
    
    n, m = map(int, input().split())
    numbers1 = list(map(int, input().split()))
    numbers2 = list(map(int, input().split()))
    
    
def is_correct(x2):
    	return not (numbers1.count(x2) == numbers2.count(x2) == 1 and oth_el2(numbers1, x2) == oth_el2(numbers2, x2))
    #
    #
    # is_correct_a1 = [[False, False] for _ in range(n)]
    # is_correct_a2 = [[False, False] for __ in range(m)]
    #
    #
# def add_it(x, a, ca):
    # 	i = a.index(x)
    # 	i1, i2 = div mod(i, 2)
    # 	ca[i1][i2] = True
    #
    #
    res = 10
    for number in set(numbers1).intersection(set(numbers2)):
    	if is_correct(number):
    		if res == 10:
    			res = number
    		else:
    			res = 0
    mode = False
    prev_correct = False
    if res == 0:
    	for ns1, ns2 in (numbers1, numbers2), (numbers2, numbers1):
    		for i in range(n*2):
    			x = ns1[i]
    			cur_correct = x in ns2 and not (ns2.count(x) == 1 and oth_el(ns1, i) == oth_el2(ns2, x))
    			if mode and prev_correct and cur_correct:
    				res = -1
    				break
    			mode = not mode
    			prev_correct = cur_correct
    		else:
    			continue
    		break
    print(res)