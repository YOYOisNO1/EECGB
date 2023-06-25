def program2672():
    
    ch=input()
    
    g=ch.count('G')
    r=ch.count('R')
    b=ch.count('B')
    
    if (g and r and b) : print('RBG')
    else if (g>1 and r>1): print ('RBG')
    else if (g>1 and b>1): print ('RBG')
    else if (r>1 and b>1): print ('RBG')
    
    else if (g=1 and r>1): print ('BG')
    else if (g=1 and b>1): print ('RG')
    else if (r=1 and b>1): print ('RG')
    else if (r=1 and g>1): print ('RB')
    else if (b=1 and r>1): print ('BG')
    else if (b=1 and g>1): print ('RB')
    
    else if (g=1 and r=1): print ('B')
    else if (g=1 and b=1): print ('R')
    else if (r=1 and b=1): print ('G')
    
    else if r : print ('R')
    else if b : print ('B')
    else if g : print ('G')
    
    