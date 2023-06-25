def program1814():
        n = int(input())
        a = int(input())
        b = int(input())
        first = n
        if n % a == 0:
            print('YES')
            print(n//a, 0)
        elif n % b == 0:
            print('YES')
            print(0, n // b)
        else:
            while n % a and n > 0:
                n -= b
            if n < 0:
                print('NO')
            else:
                print('YES')
                print(n//a, (first-n) // b)