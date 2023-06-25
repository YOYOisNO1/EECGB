def program1558():
    n=input()
    print sum(n%i==0 for i in range(1, n))