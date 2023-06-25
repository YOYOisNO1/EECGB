def program4002():
    base,num = map(int,input().split())
    if base==3 or base==2 :
        print("YES")
        quit()
        
    newNum = []
    
    while num > 0:
        newNum=[num % base] + newNum
        num //= base
    newNum=[0]+newNum
    for i in range(len(newNum)-1,0,-1) :
        if newNum[i]==base or newNum[i]==base-1 :
            newNum[i-1]+=1
            continue
        if newNum[i]>1 :
            print("NO")
            quit()
        
        
            
                
                
    print("YES")
            
    