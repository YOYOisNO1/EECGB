def isPrime(num):
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                return False
        return True
     
    a=int(input())
    x=a
    if(isPrime(x)==True):
        print(1)
    elif(x%2==0):
        print(2)
    else:
        if(isPrime(x-2)==True):
            print(2)
        else:
            print(3)