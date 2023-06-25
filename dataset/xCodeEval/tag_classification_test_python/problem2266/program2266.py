def program2266():
    t=input().split()
    (n,k)=(int(t[0]),int(t[-1]))
    p=input().split()
    if int(p[0])<=0:
        print(0)
    else:
        i=1
        s=1
        while s<n:
            if int(p[s])<=0 :
                print(i)
                break
            else:
                if s<k:
                    i=i+1
                else:
                    
                    if int(p[s])==int(p[s-1]):
                        i=i+1
                    else:
                        print(i)
                        break
            s=s+1
        if s==n:
            print(i)
            
                
                    
    
        
        