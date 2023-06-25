def program1578():
    n=int(input())
    #n=2
    ans=0
    for i in range(1,n+1):
    	ans=ans+(2<<(i-1))
    
    print(ans)