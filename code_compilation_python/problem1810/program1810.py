def HOD(a, b):
        if a * b == 0:
            return a + b
        if a > b:
            a, b = b, a
        return HOD(a, b % a)
    
def main():
        n = int(input())
        a = int(input())
        b = int(input())
        if n % HOD(a, b):
            print('NO')
        else:
            f = 0
            if a < b:
                a, b = b, a
                f = 1
            for i in range(1 + n // a):
                if (n - i * a) % b == 0:
                    print('YES')
                    if f:
                        print((n - i * a) // b, i)
                    else:
                        print(i, (n - i * a) // b)
                    return
            print('NO')
    
    main()