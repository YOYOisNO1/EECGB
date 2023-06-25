def program2267():
    n,k = map(int, input().split(" "))
    p = input().split(" ")
    
    answer = 0
    
    for a in p:
    	if int(a) >= int(p[k-1]) and int(a) != 0:
    		answer+=1
    
    print(answer)
    