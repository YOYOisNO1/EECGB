def program75():
    nCoins = int (input () )
    list = [int(x) for x in input().split()]
    
    list.sort() 
    #print((list))
    maxa = 0
    apperance = 1
    if nCoins > 1 :
        for key in range (nCoins-1):
            if list[key+1]==list[key] :
                apperance += 1
                maxa = max(maxa,apperance)
            else:
                maxa = max(maxa,apperance)
                apperance = 1 
    else:
        maxa=1
    
    print((maxa))