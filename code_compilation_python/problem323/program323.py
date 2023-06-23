def program323():
    if __name__ == '__main__':
    	n = int(input().strip(" "))
    	coins = list(map(int,input().strip(" ").split(" ")))
    	pockets = dict()
    	for coin in coins:
    		if not coin in pockets:
    			pockets[coin] = 1
    		else:
    			pockets[coin] +=1
    	print(max(list(pockets.values())))