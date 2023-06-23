def program2941():
    a = 3
    b = 3
    
    i = input()
    if i[0] == 'a' || i[0] == 'h' :
        a -= 1
    
    if i[1] == '1' || i[1] == '8' :
        b -= 1
        
    print (a*b - 1)