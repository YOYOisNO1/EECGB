def move(i, cards):
    	c1 = cards[i]
    	c2 = cards[len(cards) - 1]
    
    	if c1[0] != c2[0] and c1[1] != c2[1]: return (False, "")
    
    	cards[i] = cards.pop()
    	return (True, c1)
    
def unmove(i, orig, cards):
    	cards.append(cards[i])
    	cards[i] = orig
    
def poss(cards):
    	l = len(cards)
    	if l == 1: return True
    	
    	(done, orig) = move(l-2, cards)
    	if done:
    		if poss(cards):
    			return True
    		unmove(i, orig, cards)
    	
    	if (l <= 3): return False
    	(done, orig) = move(l-4, cards)
    	if done:
    		if poss(cards):
    			return True
    		unmove(i, orig, cards)
    	return False
    
    n = int(input())
    
    cards = input().split()
    
    if (poss(cards)):
    	print("YES")
    else:
    	print("NO")