def program2915():
    a = '.-.--'
    
    num = ''
    for i in range(len(a)):
    
    while i < len(a):
        if a[i] == '.':
            num = num + '0'
        else :
            
            if a[i+1] == '.':
                num = num + '1'
            
            else:
                num = num + '2'
            i = i + 1
        i = i + 1
                
    print(num)
            
          
    
        
    