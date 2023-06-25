    board = [[1] * 10 for i in range(10)]
    for i in range(1, 9):
        for j in range(1, 9):
            board[i][j] = 0
    pieces = input().split()
    d = 'abcdefgh'
    for i in range(len(pieces)):
        pieces[i] = (d.index(pieces[i][0]) + 1, int(pieces[i][1]))
    x, y = pieces[2]
    for i in range(-1, 2):
        for j in range(-1, 2):
            board[x + i][y + j] = 1
    
def calc_rooks(x, y, dx, dy):
        global board
        if x == 0 or x == 9 or y == 0 or y == 9:
            return
        if x + dx != pieces[2][0] or y + dy != pieces[2][1]:
            board[x + dx][y + dy] = 1
            calc_rooks(x + dx, y + dy, dx, dy)
    
    for i in range(2):
        x, y = pieces[i]
        calc_rooks(x, y, -1, 0)
        calc_rooks(x, y, 1, 0)
        calc_rooks(x, y, 0, -1)
        calc_rooks(x, y, 0, 1)
    
    k = 1
    x, y = pieces[3]
    
def printer():
        global x, y, board
        for i in range(-1, 2):
            for j in range(-1, 2):
                if board[x + i][y + j] == 0:
                    print("OTHER")
                    return
        print("CHECKMATE")
    
    printer()
        