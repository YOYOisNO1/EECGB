def program3395():
    #Kalevitch and Chess by Shiva Velingker
    
    counter = 0
    tilted = [[0,0,0,0,0,0,0,0] for x in xrange(8)]
    for x in range(0,8):
        line = input()
        if line.count("W")==0:
            counter+=1
        line = list(line)
        for y in range(0,8):
            tilted[y][x] = line[y]
    
    for x in range(0,8):
        line = tilted[x].count('W')
        if line == 0:
            counter += 1
    
    if counter==16:
        counter = 8
    print(counter)
    