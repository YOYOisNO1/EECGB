    #lucky year:
    #   no more than 1 non-zero digit
    #   e.g 100 40000 5
    
    #1000000000
    
    
def checkNum(n):
        nonzeros = 0
        for i in str(n):
            if i != "0":
                nonzeros += 1        
        if nonzeros <= 1:
            return True
        else:
            return False
    
def nextNum(n):
        length = len(str(n))
        
        first = int(str(n)[0])
        first += 1
        last = str(first)
        for i in range(length-1):
            last += "0"
        full = int(last) - int(n)
        return full
    
    print(nextNum(int(input())))
            
        