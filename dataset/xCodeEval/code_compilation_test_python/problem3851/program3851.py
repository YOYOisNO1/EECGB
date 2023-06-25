    import math
    
def same_row(new, rook):
        return new[0] == rook[0] or new[1] == rook[1];
    
def knight_hop(new, piece):
        return (math.fabs(new[1]-piece[1]) + math.fabs(new[0]-piece[0]) == 3) and !same_row(new, piece);
    
    SQ = 8
    yay = 0
    attacked = []
    for i in range(2):
        s = input()
        attacked.append((ord(s[0])-ord('a'), s[1] - 1)) #0=rook 1=knight
    
    for i in range(SQ):
        for j in range(SQ):
            curr = (i,j)
            if (!(same_row(curr, attacked[0]) or knight_hop(curr, attacked[1]) or knight_hop(curr, attacked[0]) or curr == attacked[1])):
                yay += 1
                
            
    
    print(yay)