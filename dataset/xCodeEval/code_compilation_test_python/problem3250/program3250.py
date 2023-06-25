def program3250():
    n=int(input())
    s=input()
    array = list(s)
    balanceV = 0
    balanceH = 0
    count = 0
    result = 0
    
    for i in array:
        if i == "U":
          balanceV += 1
          count += 1
        elif i == "D":
          balanceV -= 1
          count += 1
        elif i == "L":
          balanceH -= 1
          count += 1
        else:
          balanceH += 1
          count += 1
        
        if balanceV == 0 and balanceH == 0:
          result = max(result, count)
    
    return result