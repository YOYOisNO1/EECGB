def program3681():
    s1 = input("")
    s2 = input("")
    if s1 == s2:
    	print(("YES"))
    elif s1 == "monday":
    	if s2 == "thursday" or s2 == "wednesday":
    		print(("YES"))
    	else:
    		print(("NO"))
    elif s1 == "tuesday":
    	if s2 == "thursday" or s2 == "friday":
    		print(("YES"))
    	else:
    		print(("NO"))
    elif s1 == "wednesday":
    	if s2 == "friday" or s2 == "saturday":
    		print(("YES"))
    	else:
    		print(("NO"))
    elif s1 == "thursday":
    	if s2 == "saturday" or s2 == "sunday":
    		print(("YES"))
    	else:
    		print(("NO"))
    elif s1 == "friday":
    	if s2 == "sunday" or s2 == "monday":
    		print(("YES"))
    	else:
    		print(("NO"))
    elif s1 == "saturday":
    	if s2 == "monday" or s2 == "tuesday":
    		print(("YES"))
    	else:
    		print(("NO"))
    elif s1 == "sunday":
    	if s2 == "tuesday" or s2 == "wednesday":
    		print(("YES"))
    	else:
    		print(("NO"))
    else:
            print(("NO"))