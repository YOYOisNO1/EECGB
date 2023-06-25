def program1091():
    n,m,a,b = [int(i) for i in input().split()]
    if b < a:
        if n%m == 0:
            print((n/m)*b)
        else:
            print((n/m)*b) + b
    elif a*m <= b:
        print(n*a)
    elif n < m:
        print(min(b,a*n))
    else:    
        print((n/m)*b) + (n%m)*a  