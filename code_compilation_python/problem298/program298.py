def program298():
    array = []
    for i in range(3):
        array.append([item for item in input()])
    count1 = array[0].count("X")
    count2 = array[1].count("X")
    count3 = array[2].count("X")
    count4 = array[0].count("0")
    count5 = array[1].count("0")
    count6 = array[2].count("0")
    array1 = []
    array2 = []
    if count1 == 3:
        array1.append(count1)
    if count2 == 3:
        array1.append(count2)
    if count3 == 3:
        array1.append(count3)
    if count4 == 3:
        array2.append(count4)
    if count5 == 3:
        array2.append(count5)
    if count6 == 3:
        array2.append(count6)
    xcount = 0
    ocount = 0
    emptycount = 0
    countt1 = 0
    for row in array:
        for item in row:
            if item == "X":
                xcount += 1
            elif item == "0":
                ocount += 1
            elif item == ".":
                emptycount += 1
    if ocount > xcount:
        print("illegal")
    # player 1 win possibilities 
    # horizontal possibilities
    elif array[0] == ["X","X","X"]:
        print("the first player won")
    elif array[1] == ["X","X","X"]:
        print("the first player won")
    elif array[2] == ["X","X","X"]:
        print("the first player won")
    # vertical possibilities
    elif array[0][0] == "X" and array[1][0] == "X" and array[2][0] == "X":
        print("the first player won")
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        print("the first player won")
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        print("the first player won")
    # diagonal possibilies
    elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        print("the first player won")
    elif grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X":
        print("the first player won")
    
    # player2 win possibilities
    # horizontal possibilities
    elif array[0] == ["0","0","0"]:
        print("the second player won")
    elif array[1] == ["0","0","0"]:
        print("the second player won")
    elif array[2] == ["0","0","0"]:
        print("the second player won")
    # vertical possibilities
    elif array[0][0] == "0" and array[1][0] == "0" and array[2][0] == "0":
        print("the second player won")
    elif grid[0][1] == "0" and grid[1][1] == "0" and grid[2][1] == "0":
        print("the second player won")
    elif grid[0][2] == "0" and grid[1][2] == "0" and grid[2][2] == "0":
        print("the second player won")
    # diagonal possibilies
    elif grid[0][0] == "0" and grid[1][1] == "0" and grid[2][2] == "0":
        print("the second player won")
    elif grid[0][2] == "0" and grid[1][1] == "0" and grid[2][0] == "0":
        print("the second player won")
    elif xcount > ocount:
        if xcount-ocount == 1:
            print("second")
        else:
            print("illegal")
    elif array[0][0] == "X" and array[1][0] == "X" and array[2][0] == "X" and grid[0][1] == "0" and grid[1][1] == "0" and grid[2][1] == "0":
        print("illegal")
    elif array[0][0] == "X" and array[1][0] == "X" and array[2][0] == "X" and grid[0][2] == "0" and grid[1][2] == "0" and grid[2][2] == "0":
        print("illegal")
    elif array[0][0] == "0" and array[1][0] == "0" and array[2][0] == "0" and grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        print("illegal")
    elif array[0][0] == "0" and array[1][0] == "0" and array[2][0] == "0" and grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        print("illegal")
    elif ocount == xcount:
        hey = True
        for item in array1:
            if item in array2:
                print("illegal")
                hey = False
                break
        if hey == True:
            print("first")
    else:
        print("draw")
    
    
    
    
    
    
    
    