def program787():
    a,b = input().split()
    a=int(a)
    b=int(b)
    n=9999
    for i in range(1,n):
            a=a*3
            b=b*2
            if(a>b):
                    n=i
                    break
    print(n)