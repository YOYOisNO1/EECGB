    import math
def abc(n):
        global k
        if n!=0:
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    k+=1
                    n-=i
                    return abc(n)                
            else:
                k+=1
                n=0
                return abc(0)
        else:
            return print(k)
        
    n=int(input())
    k=0
    abc(n)