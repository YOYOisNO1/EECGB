    n = input()
    
def f(n):
        sumi = 0
        while n>0:
            sumi+=n%10
            n=n/10
        return sumi%4==0
        
    while True:
        if f(n):
            print(n)
            break
        else:
            n+=1