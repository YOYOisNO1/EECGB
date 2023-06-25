def program2819():
    n=int(input())
    t=(1*6+n*6)*(n/2)
    if n%2:
        t+=(n+1)/2*6
    print(1+t)