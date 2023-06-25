def program2169():
    n = input()
    a = map(int, input().split())
    b = map(int, input().split())
    
    from collections import defaultdict 
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)
    
    for e in a:
    	a_dict[e] += 1
    
    for e in b:
    	b_dict[e] += 1
    
    impossible = False
    diff_sum = 0
    for i in range(1, 6):
    	diff = abs(b_dict[i] - a_dict[i])
    	# print(i,) diff
    	if diff%2 == 1:
    		impossible = True
    		break
    	else:
    		diff_sum += diff
    
    
    if impossible:
    	print(-1)
    else:
    	print(diff_sum/4)