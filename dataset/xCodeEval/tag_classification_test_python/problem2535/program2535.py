    '''
    
    1. Figure out min number to get a kontsu
    
       Get a 'counter', count exact match.
         - 3 - find max value 
    
    2. Figure out min number to get a mentsu
    
       Sort the cards 
    
       Do a while loop
    
       While i is < len(lst)
         
         Count # of consecutive cards 
    
         Move j until index of the last consecutive card
    
    
    '''
    
def min_mentsu(cards):
        return min(min_koutsu(cards), min_shuntsu(cards))
    
def min_koutsu(cards):
        counter = {}
    
        for card in cards:
            if card not in counter:
                counter[card] = 0
            counter[card] += 1
    
        return max(0, 3 - max(counter.values()))
    
def min_shuntsu(cards):
        '''
        Cases:
    
        3 same:
    
        2 same: either consecutive 
    
        7p 8p or 7p 9p
    
    
    
        '''
    
        cards = sorted([(int(card[0]), card[1]) for card in cards], key=lambda x: (x[1], x[0]))
    
        if consecutive(cards, 0) and consecutive(cards, 1):
            return 0
    
        if consecutive(cards, 0) or consecutive(cards, 1):
            return 1
    
        if jump_consecutive(cards, 0) or jump_consecutive(cards, 1):
            return 1
    
        return 2
    
    
def consecutive(cards, i):
        num, suit = cards[i]
        num2, suit2 = cards[i + 1]
    
        return suit == suit2 and num2 - num == 1
    
def jump_consecutive(cards, i):
        num, suit = cards[i]
        num2, suit2 = cards[i + 1]
    
        r = (suit == suit2) and (num2 - num == 2)
        return r
    
    
    
    cards = input().split()
    print(min_mentsu(cards))