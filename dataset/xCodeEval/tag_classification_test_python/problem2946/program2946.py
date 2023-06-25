def sumDigit(num):
        digit=0
        while num:
            digit+=num%10
            num/=10
            
        return digit
    
    n=int(input())
    first=19
    while n>1:
        first+=9
        if sumDigit(first)==10:
            n-=1
        
    print(first)
                
            