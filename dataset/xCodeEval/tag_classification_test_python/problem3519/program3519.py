def program3519():
    A=list(map(int,input().split()))
    a=A[0]
    b=A[1]
    n=A[2]
    while n>=0:
        k=n
        if n>a:k=a
        while k>0:
            if a%k==0 and n%k==0:
                n-=k
                break
            k-=1
        if n==0:
            print("0")
            break
        k=n
        if n>b:k=b
        while k>0:
            if b%k==0 and n%k==0:
                n-=k
                break
            k-=1
        if n==0:
            print("1")
            break