    x = int(input())
    
def checker(n):
        if any(i in str(x) for i in str(n)):
            return True
        else:
            return False
    
    c = 0
    
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            c += checker(i)
            if i*i != x:
                c += checker(x//i)
    print(c)