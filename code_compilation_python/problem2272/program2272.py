def fun12(n):
        while True:
            n1=n:
            for i in range(n+1,0,-1):
                if i%2==0:
                    n1=n-i;
                    break;
            if n1==n:
                return "Ehab"
            if n1==0:
                return "Mahmoud"
            
            for i in range(n1+1,0,-1):
                if i%2==1:
                    n=n1-i;
                    break;
            
    n=int(input())
    print(fun12(n))
    
            