    from math import sqrt
def prime(n):
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
        return True
        
    n=input()
    i=1
    while True:
        if prime(n*i+1)==False:
            print(i)
            exit(0)
        i+=1