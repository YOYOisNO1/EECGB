def program2193():
    n = int(input())
    s = 0
    if 2<=n<=100000:
        for i in range(1,n):
            if n%i == 0:
                s+=1
    print(s)