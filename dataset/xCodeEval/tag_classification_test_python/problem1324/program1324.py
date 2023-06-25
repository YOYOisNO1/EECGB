def nod(a, b):
        while((a != 0) and (b != 0)):
            if a > b:
                a = a % b
            else:
                b = b % a
        return(a + b)
            
    
    n, k = map(int, input().split())
    k = 10**k
    print(int(n*k / nod(n, k)))
        
        