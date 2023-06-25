def program75():
    n = int(input())
    
    if n % 2 != 0:
        print('0')
    elif n % 4 == 0:
        print(str(n/4) - 1)
    else:
        print(str(n/4))