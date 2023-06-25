def factors(n):    
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def checkDigits(a, b):
        same = False
        a = str(a)
        b = str(b)
        for i in range(len(a)):
            if a[i] in b:
                same = True
                break
        return same
    
    num = input()
    num = int(num)
    count = 0
    factors = factors(num)
    for i in factors:
        if checkDigits(i, num):
            count += 1
    
    print(count)