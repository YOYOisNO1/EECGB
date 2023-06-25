def program1195():
    charnum=int(input())
    char=str(input())
    #if (len(char)==charnum):
    	if (len(set(char))!=len(char)):
    		print("YES")
    	else:
    		print("NO")	
    #else:
    	print("ERROR")
    
    
    