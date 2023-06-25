def program1662():
    n = int(input())
    p=0
    for i in range(2,n):
        p+=i*(i+1)
    print(p)