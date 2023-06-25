def program478():
    n=int(input())
    if n%2==0:
        for i in range(1,1000):
            if(((i*n)+1)%3==0):
                print(i)
                break
    else:
        if n==1:
            print(3)
            break
        print(1)