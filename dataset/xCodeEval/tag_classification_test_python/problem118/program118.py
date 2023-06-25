def program118():
    #codeforces_957A_live
    n = int(input())
    si = input()
    flag = True
    if "MM" in si or "CC" in si or "YY" in si or not("?" in si):
    	print("No")
    elif "???" in si or "??" in si:
    	print("Yes")
    elif si.startswith("?") or si.endswith("?"):
    	print("Yes")
    else:
    	for k in range(n):
    		if si[k] == "?" and si[k-1] == si[k+1]:
    			print("Yes")
    			flag = False
    			break;
    	if flag :
    		print("No")