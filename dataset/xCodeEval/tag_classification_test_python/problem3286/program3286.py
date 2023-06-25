def program3286():
    from math import sqrt
    n = int(input())
    for i in range(int(sqrt(n))+1,0,-1):
    
        if n%i == 0:
            a = i
            b = n//i
            if b >= a:
                print(a,b)
                break