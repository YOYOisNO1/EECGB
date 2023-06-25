def program164():
    n,m=map(int,input().split(" "))
    mini=n-(2*m)
    s=0
    maxi=0
    for i in range(n+1):
    	if ((i*(i-1))/2)>=m:
    		maxi=n-i
    		break
    
    mini=max(0,mini)
    print(mini,maxi)