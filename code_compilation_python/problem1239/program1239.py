def program1239():
    input = input().split()
    
    a= int(input[0])
    if (a < 0):
        a *= -1
    
    b= int(input[1])
    if (b < 0):
        b *= -1
    
    s= int(input[2])
    if ( a + b == s ):
        print ("Yes")
        
    elif ( a + b < s ) and ((s - (a + b)) % 2) == 0 ):
        print ("Yes")  
            
    else:
        print ("No")
        