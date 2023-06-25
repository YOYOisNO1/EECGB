def program193():
    # -*- coding: utf-8 -*-
    """
    Created on Sun May 29 08:19:41 2016
    
    @author: Dell_
    """
    
    import sys
    if False:
        input = open('program.txt', 'r')
    else:
        input = sys.stdin
        
    instructions = ['H', 'Q', '9']
    p = input.readline().strip()
    c = 0
    
    for char in p:
        if char in instructions:
            c = 1
            break
    
    if c == 1:
        print(("YES"))
    else:
        print(("NO"))