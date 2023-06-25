    x1 = input()
    x2 = input()
    
    
def change_to_date(xx):
        if (xx == "sunday"):
            return 1
        elif (xx == "monday"):
            return 2
        elif (xx == "tuesday"):
            return 3
        elif (xx == "wednesday"):
            return 4
        elif (xx == "thursday"):
            return 5
        elif (xx == "friday"):
            return 6
        elif (xx == "saturday"):
            return 7
    
    x1 = change_to_date(x1)
    x2 = change_to_date(x2)
    
    
    xx = x2 - x1
    
    if xx < 0:
        xx = xx + 7
    #print(xx)
    if xx == 3 or xx == 0 or xx == 2:
        print("YES")
    else:
        print("NO")