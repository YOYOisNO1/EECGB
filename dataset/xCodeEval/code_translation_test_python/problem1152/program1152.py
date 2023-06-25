def program1152():
    #t=int(input())
    for _ in range(1):
        a,b,c,d=map(int,input().split())
        ans=0
        for i in range(a,b+1):
            x=b+i-1
            y=c+i-1
            
            if y<c:
                pass
            elif x>d:
                m = (y-x+1)
                ans+=m*(d-c+1)
            else:
                m=max(0,y-d)
                ans+=m*(d-c+1)
                m=min(d-c+1,min(d,y)-c+1)
                if m<0:
                    pass
                else:
                    ans+=(m*(m+1))//2
                m = max(1,max(c,x)-c+1)-1
                ans-=(m*(m+1))//2
                #ans+=(m*(m+1))//2
            
                
            #ans+=(min(c,y)-max(b,x)+1)
    
    
        
        print(ans)
                
                