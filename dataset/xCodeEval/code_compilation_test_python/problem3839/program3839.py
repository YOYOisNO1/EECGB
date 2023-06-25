def program3839():
    
    str1 = '''
    Washington
    Adams
    Jefferson
    Madison
    Monroe
    Quincy Adams
    Jackson
    Van Buren
    Henry Harrison
    Tyler
    Polk
    Taylor
    Fillmore
    Pierce
    Buchanan
    Lincoln
    Johnson
    Grant
    Hayes
    Garfield
    Arthur
    Cleveland
    Harrison
    Cleveland
    McKinley
    Roosevelt
    Howard Taft
    Wilson
    Harding
    Coolidge
    Hoover
    Roosevelt
    Truman
    Eisenhower 
    Kennedy 
    Johnson 
    Nixon 
    Ford 
    Carter 
    Reagan 
    Bush 
    Clinton 
    Bush
    Obama'''
    
    
    
    str1 = str1.split('\n')
    x = input()
    
    
    
    if x in [4]:
    	raise ValueError
    
    print str1[x]