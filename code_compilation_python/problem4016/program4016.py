def program4016():
    lst=map(int, input().split())
    d = lst[0]; k = lst[1]; a = lst[2]; b = lst[3]; t = lst[4]
    
    stop = d / k
    auto_len = d 
    walk_len = 0
    min_time = auto_len * a + stop * t + walk_len * b
    
    while stop:
    	auto_len = k * stop
    	walk_len = d - auto_len
    	stop -= 1
    	min_time1 = auto_len * a + stop * t + walk_len * b
    	if min_time1 > min_time:
    		break
    	min_time = min_time1
    
    print min_time