def program4205():
    s=str(input())
    space='aeiou13579'
    c=0
    for i in s:
    	if i in space:
    		c+=1
    print(c)