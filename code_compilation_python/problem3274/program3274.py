    ##chess for tree
    ##893A
    
    
def getplayers(lst):                   ##gets the players of the first game with a different winner
        for i in range(len(lst)):
            if lst[i] != lst[0]:
                finali = i
                break
        return i, lst[0], lst[i]
    
def getnewplayer(lst):
        for i in range(1,4):
            if i is not in lst:
                return i
        
    
    
    
    
        
    
    
    
    result = "YES"
    n = input() ##number of games played
    winners = []
    for i in range(n):
        winner = input()
        winners.append(winner)
    gameandplayers = getplayers(winners)
    game = gameandplayers[0]
    players = gameandplayers[1,2]
    for i in range(game, n):
        if winners[i] is not in players:
            result = "NO"
            break
        else:
            newplayer = getnewplayer(players)
            players = (winner, newplayer)
            
    
    print(result)