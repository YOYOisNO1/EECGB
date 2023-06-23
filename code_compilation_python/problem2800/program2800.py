def buy(prices.house_index,budget):
        distance1=None
        distance2=None
        result=None
    
        for index in range(house_index-1,-1,-1):
            price=prices[index]
            if price>0 and price<=budget:
               distance1=house_index-index
        
        for index in range(house_index+1,len(prices)):
            price=prices[index]
            if price>0 and price<=budget:
               distance2=index-house_index
    
        if distance2==None or distance1<distance2:
            result=distance1*10
        else:
            result=distance2*10
        return result
    
    
    houses,house_index,budget=map(int,input().split())
    prices=list(map(int,input().split()))
    result=buy(prices.house_index,budget)
    print(result)