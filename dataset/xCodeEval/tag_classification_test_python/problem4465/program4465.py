def program4465():
    # Mariana Mendes
    # 651A - Joysticks
    
    j1,j2 = map(int, input().split(" "))
    ans = 0
    
    while True:
    	
    	if((j1 <= 0 or j2 <= 0) or (j1 == 1 and j2 == 1)):
    		 break
    	
    	if(j1 > j2):
    		j2+=1
    		j1 -=2
    	else:
    		j2-=2
    		j1+=1
    	
    	ans += 1
    print(ans)