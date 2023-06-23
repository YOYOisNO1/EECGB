def program1684():
    n = int(input())
    a = list(input())
    
    for i in range(n-1):
    	j = i+1
    	if (a[i]==a[j] and a[i]!="?") or (a[min(0,i-1)]!=a[j] and a[min(0,i-1)]!=a[min(n-1,j+1)]:
    		print("No")
    		exit()
    	
    print("Yes")
    		