def chess (board):
    	pontuation_map = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1, 'k': 0, '.': 0}
    	
    	white_weight = 0
    	black_weight = 0
    	for pos in board:
    		if pos.isupper():
    			key = pos.lower()
    			white_weight += pontuation_map[key]
    		else:
    			black_weight += pontuation_map[pos]
    			
    	if white_weight > black_weight:
    		return "White"
    	elif black_weight > white_weight:
    		return "Black"
    	else:
    		return "Draw"
    		
    board = ""
    for i in range(8):
    	e = input()
    	board += e
    	
    print(chess) (board)
    