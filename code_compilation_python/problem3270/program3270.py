def isPossible(w):
        currentPlayers = [1,2]
        allPlayers = [1,2,3]
    
        for(player in w):
            if(player in possiblePlayers):
                for(spectator in allPlayers):
                    if spectator not in currentPlayers:
                        nextPlayer = spectator
                possiblePlayers.append(nextPlayer)
                possiblePlayers.remove(player)
            else:
                return 'NO'
            
        return 'YES'
                
    
    w = []
    while True:
        line = input()
        if line:
          w.append(int(line))
        else:
            break
    
    
    print(w)
    
    print(isPossible(w))