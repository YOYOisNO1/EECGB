def program2623():
    a,b,c=input().split()
    x=[52,52,52,52,53,53,52]
    if c=='week':
    	print(x[int(a)-1])
    else:
    	if int(a)==31:
    		print(7)
    	elif int(a)==30:
    		print(11)
    	else:
    		print(12)