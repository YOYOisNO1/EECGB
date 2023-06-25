    
def area1( num):
    
        num = num -1
    
        if num == 0 :
            return 3
        elif num == 1:
            return 5
        elif num == 2:
            return 7
        elif num% 3 == 0:
            return 8 + 4 * int(num/3 -1)
        else:
            if num % 3 == 1:
    
                div = int(num/3)
                final = 8 + 4 * (div -1) + 1
                return final
                # return (8 + 4 * (int(num/3) -1) + 1
    
            else:
    
                div = int(num / 3)
                final = 8 + 4 * (div - 1) + 3
                return final
    
    
    
    number = int(input())
    
    
    
    
    print(area1(number))
    