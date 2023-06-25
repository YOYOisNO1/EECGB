def program527():
    n=int(input())
    s = ''
    n = 
    if n%2==0:
        s+='2'
    for i in range(3, n+ 1,2):
        if(n % i == 0):
            isprime = 1
            for j in range(2, (i //2 + 1)):
                if(i % j == 0):
                    isprime = 0
                    break
                
            if (isprime == 1):
                s+=str(i)
                
    print(s)        