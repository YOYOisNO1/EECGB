    n=input()
    
    
def is_power_of_2(n):
        while n>1:
            if n % 2 == 1:
                return False
            else:
                n = n/2
        return True
    
    i=0
    while i<(n+1)/2:
        if is_power_of_2(n-2*i):
            answer=i
            break
        i+=1
    
    
    print answer