def program206():
    # Online Python compiler (interpreter) to run Python online.
    # Write Python 3 code in this online editor and run it.
    
    
    ties = int(input())
    scarves = int(input())
    vest = int(input())
    jackets = int(input())
    first = int(input())
    second = int(input())
    
    if second > first:
        second_suits = min([scarves, vest, jackets]) * second
        first_suits = min([ties, jackets - min([scarves, vest, jackets])]) * first
    else:
        first_suits = min([ties, jackets]) * first
        second_suits = min([scarves, vest, jackets - min([ties, jackets])]) * second
        
    
    print(second_suits + first_suits)