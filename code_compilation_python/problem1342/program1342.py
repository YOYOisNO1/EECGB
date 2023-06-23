def program1342():
    n=int(input())
    a=list(input())
    b=list(input())
    
    count=[0 for i in range(26)]
    count1=[0 for i in range(26)]
    
    for i in range(n):
        count[97-ord(a[i])]+=1
        count1[97-ord(b[i])]+=1
    
    
    if(count!=count1):
        print(-1)
    
    i=0
    else:
        while(True):
            if(a[i]!=b[i]):
                for j in range(i+1,n):
                    if(a[j]==b[i]):
                        break
                a=a[:i]+a[]
                
            
        
    for i in range(count11):
        print(ans[i],end=" ")