def program2885():
    table = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
    n = int(input())
    s = input()
    
    res = ""
    for na in table:
    	if len(na) != n:
    		continue
    	for i in range(n):
    		if s[i] != '.' and s[i] != na[i]:
    			break
    	else:
    		res = na
    		break
    
    print(res)