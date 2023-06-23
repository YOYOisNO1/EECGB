def program1381():
    s = input()
    lucky = True
    
    for i in range(len(s)):
    	if (s[i] != 4 or s[i] != 7):
    		lucky = False
    		break
    
    if lucky:
    	print("YES")
    	else;
    	print("NO")