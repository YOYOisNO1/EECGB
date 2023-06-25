def program2550():
    a,b=map(int,input().split())
    
    if b-a>=5:
        print("0")
    elif:
        pro=1 
        for i in range(b-a):
            pro*=(b-i)
        print(pro%10)
    
        