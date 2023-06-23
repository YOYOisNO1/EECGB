    
def IsPrime(n):
        d = 2
        if n != 1:
            while n % d != 0:
                d += 1
        return d == n
    
    
    p = False
    n, m, k = [int(i) for i in input().split()]
    
    if m==2 and k==1 :
        if n%2!=0:
            print('Timur')
        else:print('Marsel')
        quit()
    if k!=1:
        for i in range(m // 2, k - 1, -1):
            if m % i == 0:
                p = True
    if p==False and k!=1:
        print('Marsel')
        quit()
    if IsPrime(m):
        print('Marsel')
    elif k >= m:
        print('Marsel')
    elif m % 2 == 0 or m % 2 != 0:
        if n % 2 != 0:
            print('Timur')
        else:
            print('Marsel')