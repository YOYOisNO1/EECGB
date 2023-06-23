def program333():
    cats  = lambda x,y: min(y,x-y) if y > 0 else 1
    
    print(cats(int(input()),int(input())))
    
    #Test Cases
    #print(cats(7,4)) = 3
    #print(cats(6,2)) = 2
    #print(cats(3,0)) = 1
    #print(cats(2,2)) = 0