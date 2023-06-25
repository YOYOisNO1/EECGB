def main():
    	for i in range(4):
    		v=[eval(input())]
    	if(v[1]+v[2]>v[3] or v[0]+v[1]>v[2]) print("TRIANGLE")
    	elif(v[0]+v[1]==v[2] or v[0]+v[1]==v[3] or v[1]+v[2]==v[3]) print("SEGMENT")
    	else print("IMPOSSIBLE")
    	
    main()