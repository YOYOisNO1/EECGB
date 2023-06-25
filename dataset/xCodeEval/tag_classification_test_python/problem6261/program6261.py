def program6261():
    n=int(input())
    
    e=10**9+7
    
    print(1if n==0else(pow(2,n-1,e)+pow(2,n*2-1,e))%e)
    
    
    
    # Made By Mostafa_Khaled