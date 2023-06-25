def program4261():
    '''input
    4 2 5 4 4 4
    '''
    l = list(map(int, input().split()))
    x = sorted([l.count(i) for i in set(l)])
    if x == [6] or x == [2, 4]:
    	print("Elephant")
    elif x == [1, 1, 4] or x == [1, 5]:
    	print("Bear")
    else:
    	print("Alien")
    
    
    
    
    
    
    
    
    