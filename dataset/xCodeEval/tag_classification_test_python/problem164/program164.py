def program164():
    n = int(input())
    p = list(map(int, input().split()))
    
    total_chet = n // 2
    total_nechet = n // 2 + n % 2
    
    # print("total_chet: {}".format(total_chet))
    # print("total_nechet: {}".format(total_nechet))
    
    hang_chet = len([item for item in p if item > 0 and item% 2 == 0])
    hang_nechet = len([item for item in p if item > 0 and item% 2 == 1])
    
    # print("hang_chet: {}".format(hang_chet))
    # print("hang_nechet: {}".format(hang_nechet))
    
    rest_chet = total_chet - hang_chet
    rest_nechet = total_nechet - hang_nechet
    
    # print("rest_chet: {}".format(rest_chet))
    # print("rest_nechet: {}".format(rest_nechet))
    # print()
    
    pred = "None"
    chet_needed_lens = []
    nechet_needed_lens = []
    
    edge_start = []
    edge_finish = []
    
    given_compl = 0
    
    mixed_count = 0
    cur_zero_count = 0
    for item in p:
    	if item == 0:
    		cur_zero_count += 1
    	else:
    		if item % 2 == 0:
    			if pred == "chet":
    				chet_needed_lens.append(cur_zero_count)
    			elif pred == "nechet":
    				if cur_zero_count > 0:
    					mixed_count += 1
    				else:
    					given_compl += 1
    			elif pred == "None":
    				edge_start = ["chet", cur_zero_count]
    			else:
    				print("Invalid State, line 40")
    			pred = "chet"
    		else:
    			if pred == "nechet":
    				nechet_needed_lens.append(cur_zero_count)
    			elif pred == "chet":
    				if cur_zero_count > 0:
    					mixed_count += 1
    				else:
    					given_compl += 1
    			elif pred == "None":
    				edge_start = ["nechet", cur_zero_count]
    			else:
    				print("Invalid state, line 50, pred = {}".format(pred))
    
    			pred = "nechet"
    
    		cur_zero_count = 0
    	edge_finish = [pred, cur_zero_count]
    
    chet_needed_lens.sort()
    nechet_needed_lens.sort()
    
    # print()
    # print("mixed_count: {}".format(mixed_count))
    # print("chet_needed_lens: {}".format(chet_needed_lens))
    # print("nechet_needed_lens: {}".format(nechet_needed_lens))
    
    i = 0
    while i < len(chet_needed_lens) and chet_needed_lens[i] <= rest_chet:
    	rest_chet -= chet_needed_lens[i]
    	i += 1
    
    chet_compl = 2 * (len(chet_needed_lens) - i)
    
    i = 0
    while i < len(nechet_needed_lens) and nechet_needed_lens[i] <= rest_nechet:
    	rest_nechet -= nechet_needed_lens[i]
    	i += 1
    
    nechet_compl = 2 * (len(nechet_needed_lens) - i)
    
    start_compl = 0
    if len(edge_start) > 0:
    	if edge_start[0] == "nechet":
    		if rest_nechet >= edge_start[1]:
    			rest_nechet -= edge_start[1]
    			start_compl += 0
    		else:
    			start_compl += 1
    	else:
    		if rest_chet >= edge_start[1]:
    			rest_chet -= edge_start[1]
    			start_compl += 0
    		else:
    			start_compl += 1
    
    # print("edge_finish: {}".format(edge_finish))
    
    finish_compl = 0
    if edge_finish[0] == "nechet":
    	if rest_nechet >= edge_finish[1]:
    		finish_compl += 0
    	else:
    		finish_compl += 1 
    elif edge_finish[0] == "chet":
    	if rest_chet >= edge_finish[1]:
    		rest_chet -= edge_finish[1]
    		finish_compl += 0
    	else:
    		finish_compl += 1
    elif edge_finish[0] == "None":
    	if n > 1:
    		finish_compl += 1
    else:
    	print("Invalid State")
    
    # print("given_compl: {}".format(given_compl))
    # print("mixed_count: {}".format(mixed_count))
    # print("chet_compl: {}".format(chet_compl))
    # print("nechet_compl: {}".format(nechet_compl))
    # print("start_compl: {}".format(start_compl))
    # print("finish_compl: {}".format(finish_compl))
    
    ans = given_compl + mixed_count + chet_compl + nechet_compl + start_compl + finish_compl
    print(ans)
    # todo: edges