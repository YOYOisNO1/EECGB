def program1671():
    n,m=[int(i) for i in input().split()]
    l=[int(i) for i in input().split()]
    
    print(0,end=" ")
    
    i=1
    for i in range(1,n):
        
        lp=sorted(l[:i])
        
        j,p=0,1
        sum=l[i]
        while ((lp[j]+sum<=m) and (j<i)):
            #print(j)
            sum+=lp[j]
            p+=1
            j+=1
            
            #print(p)
      
        print(i-j,end=" ")