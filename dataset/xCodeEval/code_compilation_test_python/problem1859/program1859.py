def program1859():
    
    cash = int(input())
    
    100D = cash // 100
    
    20D = (cash % 100) // 20
    
    10D = (cash % 100 % 20) // 10
    
    5D = (cash % 100 % 20 % 10) // 5
    
    1D = (cash % 100 % 20 % 10 % 5)
    
    
    print (100D + 20D + 10D + 5D + 1D)
           
           
           