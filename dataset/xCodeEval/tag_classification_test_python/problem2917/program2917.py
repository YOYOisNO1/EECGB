    import math
def SieveofEratosthenes(number):
        prime_list = []
        prime = number
        for i in range(2,int(math.sqrt(number))+3,1): 
            if(number%i==0):
                prime = i
                break
    
        while(number > 1):
            if(number % prime == 0):
                number = number // prime
            else:
                break
        if(number == 1):
            return prime
        else:
            return 1
                
         
        return prime_list
     
     
    num = int(input())
    if(num == 1):
        print(num)
    else:
        print(SieveofEratosthenes(num))
        