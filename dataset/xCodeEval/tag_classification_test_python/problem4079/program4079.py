def program4079():
    import math
    inp = int(input())
    
    if inp == 1:
        print("0 1")
    
    elif inp % 7 == 0:
        both = inp // 7 * 2
        print(both, both)
    
    elif inp % 7 == 6:
        maxim = math.ceil(inp / 7) * 2 
        minim = math.ceil(inp / 7) * 2 - 1
        print(minim, maxim)
    
    elif inp % 7 == 1:
        maxim = int(inp / 7) * 2 + 1
        minim = int(inp / 7) * 2
        print(minim, maxim)
    
    elif inp % 7 == 2 or inp % 7 == 3 or inp % 7 == 4 or inp % 7 == 5:
        maxim = math.ceil(inp / 7) * 2
        minim = maxim - 2
        print(minim, maxim)