def program1320():
    n=int(input())
    for i in range(n):
        p=int(input())
        for i in range(1,101):
            if (p%i==0 and (100-p)%i==0):
        p=p/i
        p2=(100-p)/i
        print(p+p2)