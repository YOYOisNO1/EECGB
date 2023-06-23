def program3432():
    pos = input().split()
    ranks = 'abcdefgh'
    intPos = []
    for piece in pos:
        intPos.append([ranks.index(piece[0]),int(piece[1])-1])
     
    guarded = []
    shift = 1
    while intPos[0][0] + shift < 8:
        square = [intPos[0][0]+shift,intPos[0][1]]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift += 1
     
    shift = -1
    while intPos[0][0] + shift >= 0:
        square = [intPos[0][0]+shift,intPos[0][1]]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift -= 1
     
    shift = 1
    while intPos[1][0] + shift < 8:
        square = [intPos[1][0]+shift,intPos[1][1]]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift += 1
     
    shift = -1
    while intPos[1][0] + shift >= 0:
        square = [intPos[1][0]+shift,intPos[1][1]]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift -= 1
     
    shift = 1
    while intPos[0][1] + shift < 8:
        square = [intPos[0][0],intPos[0][1]+shift]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift += 1
     
    shift = -1
    while intPos[0][1] + shift >= 0:
        square = [intPos[0][0],intPos[0][1]+shift]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift -= 1
     
    shift = 1
    while intPos[1][1] + shift < 8:
        square = [intPos[1][0],intPos[1][1]+shift]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift += 1
     
    shift = -1
    while intPos[1][1] + shift >= 0:
        square = [intPos[1][0],intPos[1][1]+shift]
        if square == intPos[2]:
            break
        guarded.append(square)
        shift -= 1
     
    for x in range(-1,2):
        for y in range(-1,2):
            square = [intPos[2][0]+x,intPos[2][1]+y]
            guarded.append(square)
     
    mate = True
    for x in range(-1,2):
        for y in range(-1,2):
            square = [intPos[3][0]+x,intPos[3][1]+y]
            if square[0] < 8 and square[0] >= 0:
                if square[1] < 8 and square[1] >= 0:
                    if square not in guarded:
                        mate = False
     
    if mate:
        print("CHECKMATE")
    else:
        print("OTHER")