    from sys import argv
    script,first_row,first_column,last_row,last_column = argv
    
    first_row = int(first_row)
    first_column = int(first_column)
    last_row = int(last_row)
    last_column = int(last_column)
    
def move_king(king_row,king_column):
        moves = 0
        
        while(king_row != last_row and king_column != last_column):
            king_row += min(max(-1,last_row-king_row),1)
            king_column += min(max(-1,last_column-king_column),1)
            moves += 1
        while(king_row != last_row):
            king_row += min(max(-1,last_row-king_row),1)
            moves += 1
        while(king_column != last_column):
            king_column += min(max(-1,last_column-king_column),1)
            moves += 1
        return moves
    
def move_bishop(bishop_row,bishop_column):
            moves = 0
            if((bishop_row + bishop_column)%2 != (last_row+last_column)%2):
                return 0
            if(bishop_row + bishop_column == last_row + last_column or last_row - bishop_row == last_column - bishop_column):
                return 1
            else:
                return 2
                
def move_rook(rook_row,rook_column):
        moves = 0
        if(rook_row != last_row and rook_column != last_column):
            return 2
        if(rook_row == last_row and rook_column == last_column):
            return 0
        else:
            return 1
    king_moves = move_king(first_row,first_column)
    bishop_moves = move_bishop(first_row,first_column)
    rook_moves = move_rook(first_row,last_row)
    print "%d %d %d" %(rook_moves,bishop_moves,king_moves)