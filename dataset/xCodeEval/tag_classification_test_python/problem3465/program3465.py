def program3465():
    n = int(input())
    
    
    st = input()
    ans = ''
    che  = False
    j = 0
    for i in range(len(st)):
        if st[i] == 'o' and j == i:
            if i+1 < len(st) and st[i+1] == 'g' and i+2 < len(st) and st[i+2] == 'o':            
                ans += '*' * 3
                j = i + 3
                che = True
            else:
                ans += st[i]
                j = i + 1
                che = False
        elif i == j and  st[i-1]=='o' and che == True and i+1 < len(st):
            if st[i] == 'g' and st[i+1]=='o':
                j = i + 2
                
                continue
            else:
                j = i + 1
                che = False
                ans+=st[i]
        elif che == True and j != i:
            
            continue
        else:
            ans+=st[i]
            che = False 
            j = i + 1
        
        
    print(ans)    