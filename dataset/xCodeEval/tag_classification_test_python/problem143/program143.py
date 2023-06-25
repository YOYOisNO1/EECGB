def program143():
    
    n = int(input())
    
    ls = list(map(int,input().split()))
    
    if sum(ls)/n >= 4.5 :
        
        print(0)
        
    else :
        ls.sort()
        k = 0
        cnt = 0
        
        while(sum(ls)/n<4.5) :
            
            if ls[k]<5 :
                
                ls[k]=5
                
            k += 1
            cnt = cnt + 1
            
        print(cnt)
            
            