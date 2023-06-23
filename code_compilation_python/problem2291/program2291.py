def program2291():
    n=int(input())
    while(n):
        l=list(map(int,input().split()))
        k=(l[1]-l[0])*(l[1]+l[0])
        number = k
        j=0
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    print(number, "is not a prime number")
                    j=4
                    break
            else:
                j=3
                print(number, "is a prime number")
        else:
            j=4
            print(number, "is not a prime number")
        if j==3:
            print("YES")
        else:
            print("NO)