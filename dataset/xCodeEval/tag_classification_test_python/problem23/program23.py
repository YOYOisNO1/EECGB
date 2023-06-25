def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    
        return True
    
    n = int(input())
    if n==1:
        print(3)
    elif n==2:
        print(4)
    elif n ==3:
        print(1)
    elif n ==4:
        print(2)
    elif n ==5:
        print(1)
    elif n ==6:
        print(4)
    else:
        m = 1
        while True:
            if not isPrime(n*m + 1):
                print(m)
                break
            m = m+1