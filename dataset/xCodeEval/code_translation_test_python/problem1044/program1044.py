def solve(board):
      for row in board:
        for i in range(1, 8):
          if row[i] == row[i-1]:
            return False
      return True
    
    board = [input() for i in range(8)]
    print('YES') if solve(board) else 'NO'