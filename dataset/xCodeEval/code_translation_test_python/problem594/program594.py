def program594():
    t=list(map(int,input().split()))
    s=list(map(int,input().split()))
    sum=i=0
    for i in range(t[0]):
        sum=sum+s[i]
        if i !=t[0]-1:
            sum=sum+10
    if sum<=t[1]:
        print((t[0]-1)*2+int((t[1]-sum)/5))
    else:
        print(-1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    