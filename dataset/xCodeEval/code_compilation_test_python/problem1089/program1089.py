def program1089():
    n =int(input ())
    if n <= 127:
        print ("byte")
    elif n <=32768: 
        print ("short") 
    elif n <=2147483648:
        print ("long")
    else: 
        print ("BigInteger)
    
     
    
    
    
    
    