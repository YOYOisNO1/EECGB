def program653():
    suit = ['S', 'H', 'D', 'C']
    rank = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    trump = str(input())
    cards = str(input())
    
    win = False
    
    if cards[1] == cards[4] and rank.index(cards[0]) > rank.index(cards[3]):
        win = True
        
    if cards[1] == trump
        win = True
        
    if win:
        print('YES')
    else:
        print('NO')