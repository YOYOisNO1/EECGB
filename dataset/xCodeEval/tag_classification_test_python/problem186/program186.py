def program186():
    n=int(input())
    h,a=[],[]
    result=0
    for i in range(n):
    		game=input().split()
    		h.append(game[0])
    		a.append(game[1])
    for i in range(n):
    	for j in range(n):
    		if i!=j and h[i]==a[j]:
    			result+=1
    print(result)