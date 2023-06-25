def program4670():
    arr = list(map(int,input().split()))
    total_g = arr[0]
    guards = arr[1]
    close_gate = dict()
    entry = input()
    changes = 0
    
    for i in range(0,total_g):
        if entry[i] in close_gate:
            close_gate[entry[i]] = close_gate[entry[i]] + 1
        else:
           close_gate[entry[i]] =  1
    
    cnt_gate = dict()
    avg = guards
    flag = 0
    
    for i in range(0,total_g):
        # print(entry[i])
        if entry[i] not in cnt_gate:
            if avg==0 and i!=0 and cnt_gate[entry[i-1]] != close_gate[entry[i-1]]:
                print('YES')
                flag = 1 
                break
            
            # print("new gate opened")
            cnt_gate[entry[i]] = 1 
            avg = avg -1
            # print(cnt_gate[entry[i]],close_gate[entry[i]])
            # print('guards available',avg)
            if cnt_gate[entry[i]] == close_gate[entry[i]]:
                avg = avg + 1 
            
        else :
            cnt_gate[entry[i]] = cnt_gate[entry[i]] + 1 
            if cnt_gate[entry[i]] == close_gate[entry[i]]:
                # print('gate was',entry[i], 'closed')
                avg = avg + 1 
                
    if flag == 0:
        print('NO')
            
    
    
             
                
    
        
    
        
        
        
        
        