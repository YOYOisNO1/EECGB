def program320():
    n = int(input())
    
    coins = map(int, input().split())
    
    coinDict = {}
    
    for i in range(len(coins)):
    	if coins[i] not in coinDict:
    		coinDict[coins[i]] = 1
    	else:
    		coinDict[coins[i]] += 1
    
    print max(coinDict.values())