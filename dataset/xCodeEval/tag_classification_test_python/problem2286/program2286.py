def program2286():
    n = int(input())
    if n == 0:
        print("O-|-OOOO")
    else :
        while n > 0:
            d = n % 10
            n //= 10
            if d < 5:
                print('O-|', 'O' * d, '-', 'O' * (4-d), sep='')
            else :
                d -= 5
                print('-O|', 'O' * d, '-', 'O' * (4-d), sep='')