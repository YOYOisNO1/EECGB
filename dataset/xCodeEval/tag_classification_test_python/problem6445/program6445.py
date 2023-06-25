def program6445():
    
    #a=list(map(int,input().split()))
    
    #y,x=map(int,input().split())
    
    n=int(input())
    cnt=0
    
    for c in range(1,n+1):
        for b in range((c+1)//2,c+1):
            a=c^b
            if a<=b and a+b>c:
                cnt+=1
    
    print(cnt)