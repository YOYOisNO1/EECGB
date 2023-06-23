def program324():
    #highest frequency approach - n pockets
    I = input
    n = int(I())
    coins = I().split()
    print(max([coins.count(coin) for coin in coins]))
    
    #####( 2 pockets solution =( )######################
    #for i in range(0,n):
    #	if coins[i] not in A:
    #		A.append(coins[i])
    #	else:
    #		B.append(coins[i])
    #if len(A) > 0 and len(B)>0:
    #	print(2)
    #else:
    #	print(1)