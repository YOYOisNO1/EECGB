def program445():
    
     R=lambda:map(int,input().split())
    n,k=R()
    print max(0,(k*2-1)*n-sum(R())*2)