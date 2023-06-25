def check_Rows(board, row, sym):
        if board[row][0] == sym and board[row][1] == sym and board[row][2] == sym:
            return True
        return False
    
def check_Cols(board, col, sym):
        if board[0][col] == sym and board[1][col] == sym and board[2][col]== sym:
            return True
        return False
    
def check_Diagonal(board, sym):
        if board[0][0] == sym and board[1][1] == sym and board[2][2] == sym:
            return True
        return False
    
def check_Reverse_Diagonal(board, sym):
        if board[0][2] == sym and board[1][1] == sym and board[2][0] == sym:
            return True
        return False
    
def check_Wins(board, sym):
        i=0
        #check rows
        while i < 3:
            if check_Rows(board, i, sym):
                return True
            i+=1
    
        #check cols
        i=0
        while i < 3:
            if check_Cols(board, i, sym):
                return True
            i+=1
    
        #check diagonal and reversediagonal
        if check_Diagonal(board, sym):
            return True
        elif check_Reverse_Diagonal(board, sym):
            return True
    
        return False
    
def is_Full(board):
        if board[0].count('.') == 0 and board[1].count('.') == 0 and board[2].count('.') == 0:
            return True
        return False
    
def check_Chance(board):
        cntx = 0
        cnt0 = 0
        cntx = board[0].count('X') + board[1].count('X') + board[2].count('X')
        cnt0 = board[0].count('0') + board[1].count('0') + board[2].count('0')
        if cntx > cnt0:
            return 'second'
        elif cntx == cnt0:
            return 'first'
        return False
    
    board = []
    board.append(list(input()))
    board.append(list(input()))
    board.append(list(input()))
    
    cntx = board[0].count('X') + board[1].count('X') + board[2].count('X')
    cnt0 = board[0].count('0') + board[1].count('0') + board[2].count('0') 
    
    if check_Wins(board, 'X') and check_Wins(board, '0'):
        print('illegal')
    elif cnt0 > cntx or (cntx > cnt0 and cntx!=cnt0+1):
        print('illegal')
    elif check_Wins(board, '0') and cntx!=cnt0:
        print('illegal')
    elif check_Wins(board, 'X') and cntx-1!=cnt0:
        print('illegal')
    elif check_Wins(board, 'X'):
        print('the first player won')
    elif check_Wins(board, '0'):
        print('the second player won')
    elif is_Full(board):
        print('draw')
    else:
        chance = check_Chance(board)
        if chance:
            print(chance)