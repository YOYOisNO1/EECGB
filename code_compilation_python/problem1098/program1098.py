def program1098():
    a, b = map(int,input().split()))
    
    total_burned = a
    current_candles= a
    
    
    while True：
    
        if current_candles < b:
            break
        
        new_candles= current_candles/b
        left = current_candles%b
        total_burned += new_candles
        current_candles =new_candles + left
     
     print total_burned
    
        
        