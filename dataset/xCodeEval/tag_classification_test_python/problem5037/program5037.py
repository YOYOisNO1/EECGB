    w, b = map(int, input().strip().split(" "))
    
    results = {}
    total = 0.0
    
def princess_wins(w, b, princess_turn=True):
    	if (w, b) in results:
    		return results[(w, b)]
    	if w == 0 or w + b == 0:
    		return 0
    	if b == 0:
    		return int(princess_turn)
    	prob_white = w / (w + b)
    	if princess_turn:
    		res = prob_white + (1 - prob_white) * princess_wins(w, b-1, not princess_turn)
    	else:
    		#print((w, b))
    		if b == 1.0:
    			res = (1 - prob_white)
    		else:
    			prob_white_after = w / (w + b - 1)
    			res = (1 - prob_white) * ((1 - prob_white_after) * princess_wins(w, b-2, not princess_turn) + prob_white_after * princess_wins(w-1, b-1, not princess_turn))
    	results[(w, b)] = res
    	return res
    
    print(princess_wins(float(w), float(b)))