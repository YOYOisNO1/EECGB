def program2309():
    n=int(input())
    if n%2==0:
        if n//2%2==0:
            print(n//2-1,n-n//2+1)
        else:
            print(n//2-2,n-n//2+2)
    else:
        print(n//2,n-n//2)