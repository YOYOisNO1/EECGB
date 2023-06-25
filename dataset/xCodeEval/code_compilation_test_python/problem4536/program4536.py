    n,k,order = input()
def calculateMinCost(n,k,order):
    	cost = 0
    	books = []
    	day = 0
    	for ai in order:
    		if ai not in books:
    			if len(books) < k:
    				cost += 1
    				books.append(ai)
    			else:
    				needed = order[(day):(day+k)]
    				for book in books:
    					if book not in needed:
    						books.remove(book)
    				cost += 1
    				books.append(ai)
    		day += 1
    	return cost