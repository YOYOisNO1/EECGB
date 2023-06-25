def program1704():
    white = {"Q": 9, "R": 5, "B": 3, "N": 3"P": 1}
    black = {"q": 9, "r": 5, "b": 3, "n": 3, "p": 1}
    white_score = black_score = 0
    for i in range(8):
        line = input()
        for j in range(8):
            if line[j] in black:
                black_score += black[line[j]]
            elif line[j] in white:
                black_score += white[line[j]]
    
    if black_score > white_score:
        print("Black")
    elif white_score > black_score:
        print("White")
    else:
        print("Draw")