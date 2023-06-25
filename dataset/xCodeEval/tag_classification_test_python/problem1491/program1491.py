def program1491():
    s = input().split()
    chords = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H']
    c1 = chords.index(s[0])
    c2 = chords.index(s[1])
    c3 = chords.index(s[2])
    #print(c1,c2,c3)
    printed = False 
    possibilities = [[c1,c2,c3],[c2,c1,c3],[c1,c3,c2],[c2,c3,c1],[c3,c1,c2],[c3,c2,c1]]
    
    for t in possibilities:
        #print(t)
        
        if (t[0]+4)%12 == t[1] and (t[0] + 7)%12 == t[2] :
            print('major')
            printed = True
            break
            
        if (t[0]+3)%12 == t[1] and (t[0] + 7)%12 == t[2]:
            print('minor')
            printed = True
            break
        
    if not printed:
        print('strange')