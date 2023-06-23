def program3125():
    n = int(input())
    if(n % 2 != 0):
        print(0)
    else:
        if(n == 2):
            print(2)
        else:
            a = 2
            for(i in range(int(n/2) - 1)):
                a *= 2
            print(a)