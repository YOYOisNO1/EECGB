def program1810():
    friendHouseX = int(input())
    
    minimumAmountOfSteps = int(friendHouseX / 5)
    
    if friendHouseX % 5 != 0:
      minimumAmountOfSteps += 1
    
    print(minimumAmountOfSteps)