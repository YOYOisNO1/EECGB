    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Fri Jan 17 15:11:07 2020
    
    @author: thom
    """
    
    pos_rook = input()
    pos_knight = input()
    
    #pos_rook = "a1"
    #pos_knight = "b2"
    
    import string
    letter_rook = string.ascii_lowercase.index(pos_rook[0])
    number_rook = int(pos_rook[1])
    
    letter_knight = string.ascii_lowercase.index(pos_knight[0])
    number_knight = int(pos_knight[1])
    
    #rook = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
    #        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    rook = [[0 for i in range(8)] for j in range(8)]
    knight = [[0 for i in range(8)] for j in range(8)]
    
def prohibit_knight (board, letter, number):
        for i in range(8):
            for j in range(8):
                if ((i - letter)**2 + (j-number)**2) == 5:
                    board[i][j] = 1
        return(board)
    
def prohibit_rook (board, letter, number):
        prohibit_knight(board, letter, number)
        for i in range(8):
            board[letter][i] = 1
        for i in range(8):
            board[i][number] = 1
        return(board)
    
    v1 = prohibit_knight(knight, letter_knight, number_knight)
    v2 = prohibit_rook(rook, letter_rook, number_rook)
    v3 = [[0 for i in range(8)] for j in range(8)]
    count = 0
    for i in range(8):
        for j in range(8):
            v3[i][j] = v1[i][j] or v2[i][j]
            count = count + v3[i][j]
    print(64 - count)