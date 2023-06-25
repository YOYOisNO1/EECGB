def program945():
    n = int(input())
    if n <=9:
        print(n)
    elif n<=189:
        n -= 9
        a = n/2
        b = n%2
        if b==1:
            print(str(9+a+1)[0])
        else:
            print(str(9+a)[1])
    elif n<=2889:
        n -=189
        a = n/3
        b = n%3
        if b>0:
            print(str(int(99+a+1))[b-1])
        else:
            #print(str(99+a))
            print(str(int(99+a))[-1:])
    elif n<=38889:
        n -=2889
        a = n/4
        b = n%4
        if b>0:
            print(str(int(999+a+1))[b-1])
        else:
            print(str(int(999+a))[-1:])
    else:
        n -= 38889
        a = n / 5
        b = n % 5
        if b > 0:
            print(str(int(9999 + a + 1))[b - 1])
        else:
            print(str(int(9999 + a))[-1:])