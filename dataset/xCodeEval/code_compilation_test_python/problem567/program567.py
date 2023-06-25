def program567():
    str = input()
    upper=0
    lower=0
    for i in range(0,len(str)):
    	if str[i]>=65 and str[i]<=90:
    		upper+=1
    	else
    		lower+=1
    
    if upper>lower:
    	print(str.upper())
    else:
    	print(str.lower())