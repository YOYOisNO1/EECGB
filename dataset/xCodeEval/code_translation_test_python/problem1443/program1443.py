def program1443():
    a,b,c=map(int,input().split())
    if a+b<=c:
        print(c+1-(a+b))
    elif a+c<=b:
        print(b + 1 - (a + c))
    elif b+c<=a:
        print(a + 1 - (c + b))
    else:
        print(0)