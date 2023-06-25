def gcd(a, b):
        while b:
           a, b = b, a%b
        return a
    
    numbers = list(map(int,input().split()))
    
    if (numbers[0]+1 == numbers[1]):
        print(numbers[0]
    else
        print(1)
    print(gcd(numbers[0],numbers[1]))