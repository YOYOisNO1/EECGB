def program457():
    # n = int(input())
    a,b = map(long, input().split())
    
    if(a==0 or b==0):
        print("{} {}").format(a,b)
    while(1):
        if(a==0 or b==0):
            print("{} {}").format(a,b)
            exit(0)
        elif(a >= (2*b)):
            a %= (2*b)
        elif(b >= (2*a)):
            b %= (2*a)
        else :
            print("{} {}").format(a,b)
            exit(0)