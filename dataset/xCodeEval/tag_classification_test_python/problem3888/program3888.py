    import math
    
def go(i):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                print(n//i,n-n//i)
                return
        print(1,n-1)
    
    t=int(input())
    for x in range(t):
        n=int(input())
        go(n)