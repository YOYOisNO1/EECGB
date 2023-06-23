def def L(number):
        if number == 0 :
            return False
        while number > 0 :
            x = number % 10 
            number /= 10 
            if x != 7 or x!= 4 :
                return False
            
        return True
    x = int(input())
    C_7=0
    C_4=0
    C=0
    while x > 0 :
        y=x%10
        x/=10
        if y == 7:
            C_7+=1
        elif y==4:
            C_4+=1
        else :
            C+=1
    if C != 0:
        print 'NO'
    elif L(C_7+C_4) :
        print 'YES'
    else :
        print 'NO'