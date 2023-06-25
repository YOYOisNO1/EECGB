    import math
    
def cool(n):
        if n==1 || n==3:
            return "NO"
        if n==2:
            return "YES"
        for k1 in range(int(math.sqrt(n))):
            k2 = int(math.sqrt((n - (k1*(k1+1))/2)*2))
            if (k1*(k1+1))/2 + (k2*(k2+1))/2 == n:
                return"YES"
                break
            else:
                continue
        return "NO"
            
    num = int(input())
    print(cool(num))