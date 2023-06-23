def check_win():
        for i in range(3):
            if abc[i] < xyz[i]:
                return False
        return True
    
def check_can_combine_single(i):
        if abc[i] >= xyz[i] + 2:
            return True
    
def check_can_combine():
        for i in range(3):
            if check_can_combine_single(i):
                return True
    
    abc = input().split() # what he has
    xyz = input().split() # what he needs
    
    for i in range(3):
        abc[i] = int(abc[i])
        xyz[i] = int(xyz[i])
    
    while check_can_combine():
        for i in range(3):
            if abc[i] < xyz[i]: # needs to be combound
                for i_ in range(3):
                    if abc[i_] >= xyz[i_] + 2: # can afford to lose 2
                        abc[i_] = abc[i_] - 2
                        abc[i] = abc[i] + 1
    
    
    winner = check_win()
    
    if winner:
        print 'YES'
    else:
        print 'NO'