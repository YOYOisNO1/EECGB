def program2282():
    n = input()
    flag = 0
    for i in range(0,len(n)-2):
    	if set[i:i +3] == set("ABC"):
    		flag = 1
    	    break
    if(flag):
    	print("YES")
    else:
    	print("NO")