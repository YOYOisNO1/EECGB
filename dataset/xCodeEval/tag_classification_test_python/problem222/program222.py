    a = list(map(int, input().strip().split()))
    
    
def move(b, bin_index):
        board = b[:]
        amount = board[bin_index]
        board[bin_index] = 0
    
        if amount < 1:
            return board
    
        f14s = amount // 14
        amount = amount % 14
    
        if f14s:
            for i in range(len(board)):
                board[i] += f14s
    
        while amount > 0:
            next_index = (bin_index + 1) % 14
            board[next_index] += 1
            amount -= 1
            bin_index += 1
    
        return board
    
    
def score(board):
        total = 0
        for board_bin in board:
            if board_bin % 2 == 0:
                total += board_bin
        return total
    
    
    max_score = -1
    for i in range(len(a)):
        max_score = max(score(move(a, i)), max_score)
    
    print(max_score)