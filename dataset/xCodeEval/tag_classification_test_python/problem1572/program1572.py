def program1572():
    k = input()
    lst = map(int,input().split())
    sum = sum1 = 0
    lst = sorted(lst,reverse=True)
    for i in lst:
        sum += i
    
    if k==0:
        print(0)
        
    elif sum<k:
        print(-1)
        
    else:
        for ind,i in enumerate(lst):
            sum1 += i
            if sum1>=k:
                print(ind+1)
                exit(0)
            else:
                continue   
                        
            
        
        