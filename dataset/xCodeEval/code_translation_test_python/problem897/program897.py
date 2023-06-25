def program897():
    n,m = map(int,input().strip().split(' '))
    l=[]
    count = 0
    countr = 0
    countc = 0
    for i in range(n):
        l.append(input().strip())
        if 'S' not in l[i]:
            count += m
            countr += 1
    
    for j in range(m):
        flag = True
        for i in range(n):
            if l[i][j] == 'S':
                flag = False
                break
        if flag: 
            count += n
            countc += 1
    print(count) - countr*countc
    
        
    
    
    
    
    
            
    
        
    