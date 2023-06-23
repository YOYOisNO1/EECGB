def program566():
    str = input()
    
    
    lower = 0
    for i in range(len(str)):
        if(str[i] >= 'a' && str[i] <= 'z'):
            lower += 1
            if(lower >= len(str)):
                print(str.lower())
                break
            
            
    print(str.upper())